import os
from typing import Iterable, Dict, List, Optional, Tuple
import secrets
import string
import shutil

from rich.console import Console


class FileParser:
    STARTSWITH = '{&'
    ENDSWITH = '&}'

    def __init__(self, path: str):
        self._path = path

    @staticmethod
    def is_variable(line: str) -> Optional[Tuple[int, int]]:
        start = line.find(FileParser.STARTSWITH)
        if start != -1:
            end = line.find(FileParser.ENDSWITH, start)
            if end != -1:
                return start, end
        return None

    @property
    def variables(self) -> Iterable[str]:
        file = open(self._path)
        while True:
            line = file.readline()
            if not line:
                break
            result = self.is_variable(line)
            if result is not None:
                yield line[result[0] + 2:result[1]].strip()
        file.close()
        return []

    def replace_variables(self, answers):
        tmp_file = f'{self._path}.out'
        fin = open(self._path)
        fout = open(tmp_file, 'w')
        for line in fin:
            var = FileParser.is_variable(line)
            if var is not None:
                start, end = var
                key = line[start: end].replace(self.STARTSWITH, '').strip()
                line = line.replace(line[start:end + 2], answers.get(key))
            fout.write(line)
        fin.close()
        fout.close()
        shutil.move(tmp_file, self._path)


class DirectoryList:
    EXTENSIONS = ('.py', '.yml', '.conf', '.sql', '.md', '.env')

    def __init__(self, root: str):
        self._root = root
        self._vars: Dict[str, List[str]] = {}

    @property
    def files(self):
        for root, directories, files in os.walk(self._root, topdown=False):
            for name in files:
                if name.endswith(self.EXTENSIONS):
                    yield os.path.join(root, name)

    @property
    def variables(self):
        for path in self.files:
            variables = FileParser(path).variables
            for var in variables:
                if var:
                    if var in self._vars:
                        self._vars[var].append(path)
                    else:
                        self._vars[var] = [path]
        return self._vars

    def variable_to_value(self, answers):
        for path in self.files:
            FileParser(path).replace_variables(answers)


class UIView(Console):
    _CATEGORIES = {
        'Project settings': ['PROJECT_NAME', 'PROJECT_DESCRIPTION', 'PROJECT_CONTACT_EMAIL',
                             'PROJECT_TIME_ZONE', 'PROJECT_SECRET_KEY'],
        'Database settings': ['DATABASE_NAME', 'DATABASE_USER', 'DATABASE_PASSWORD'],
        'Docker settings': ['CONTAINER_PREFIX', 'SERVER_DOMAIN'],
        'Generating project': ['TEMPLATE_PATH']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answers = {}

    def menu(self):
        self.clear()
        self.print('\n[bold green]█▀▄   █ ▄▀█ █▄ █ █▀▀ █▀█ [/] [bold blue] ▀█▀ █▀▀ █▀▄▀█ █▀█ █   ▄▀█ ▀█▀ █▀▀[/]',
                   justify='center')
        self.print('[bold green]█▄▀ █▄█ █▀█ █ ▀█ █▄█ █▄█ [/] [bold blue]  █  ██▄ █ ▀ █ █▀▀ █▄▄ █▀█  █  ██▄[/]\n',
                   justify='center')

    def view_answered_question(self):
        self.menu()
        for category in self.answers:
            self.print()
            self.rule(f'[bold red] {category}')
            for question in self.answers[category]:
                self.print(f'{question["title"]}[bold green]{question["answer"]}[/]')

    @staticmethod
    def generate_password():
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(24))

    def get_answers(self, questions: Dict[str, str]):
        for category in self._CATEGORIES:
            self.print()
            self.rule(f'[bold red] {category}')
            for key in self._CATEGORIES[category]:
                if key in questions:
                    user_input = self.input(questions[key])
                    if not user_input and questions[key].find('🔑') != -1:
                        user_input = self.generate_password()
                    answer = {'title': questions[key], 'key': key, 'answer': user_input}
                    if category in self.answers:
                        self.answers[category].append(answer)
                    else:
                        self.answers[category] = [answer]
                    self.view_answered_question()


def main():
    questions = {
        'PROJECT_NAME': '💡 Enter a project name: ',
        'PROJECT_DESCRIPTION': '💡 Enter a project description: ',
        'PROJECT_CONTACT_EMAIL': '📧 Enter a contact email: ',
        'PROJECT_TIME_ZONE': '🕐 Enter a timezone: ',
        'PROJECT_SECRET_KEY': '🔑 Enter a project secret key (pass if u want to generate): ',
        'DATABASE_NAME': '💿 Enter a database name: ',
        'DATABASE_USER': '👨 Enter a database username: ',
        'DATABASE_PASSWORD': '🔑 Enter a database password (pass if u want to generate): ',
        'CONTAINER_PREFIX': '💡 Enter a container prefix: ',
        'SERVER_DOMAIN': '💡 Enter a domain: ',
        'TEMPLATE_PATH': '💡 Enter a project directory path: ',
    }

    view = UIView()
    view.menu()
    view.get_answers(questions)
    result = []
    for item in view.answers.values():
        result += item
    answers = {x['key']: x['answer'] for x in result}
    project_dir = answers['TEMPLATE_PATH']

    shutil.copytree('./template', project_dir)  # Clone template to project dir

    DirectoryList(project_dir).variable_to_value(answers)


if __name__ == '__main__':
    main()


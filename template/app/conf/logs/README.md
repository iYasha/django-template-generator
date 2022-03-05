# Логирование

Для логирования используется переделанный fork библиотеки [django-request-logging](https://github.com/Rhumbix/django-request-logging)

Логируются:
* Сброс запроса
* Хедеры
* Тело запроса
* Ответ от сервера
* IP
* Время
* Метод
* Путь
* Пользователь
* Код ответа
* View который обрабатывал запрос

Пример:
```
INFO 2021-02-10 14:23:10,913 middleware.py:log:40 - Response | Method: GET | Path: /department/ | Ip: 172.21.0.1 | User: +380666666666 | Test | Status Code: 200 | Func: DepartmentViewSet
```

Название файла состоит из `main_ГОД_МЕСЯЦ_ДЕНЬ.log`
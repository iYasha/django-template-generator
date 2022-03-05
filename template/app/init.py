import os
import logging

from django.db import connection
from django.core.management import call_command
from django.conf import settings
from io import StringIO
from conf import wsgi
import django


logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')

logging.info("Performing migrations")
call_command('makemigrations')
call_command('migrate')


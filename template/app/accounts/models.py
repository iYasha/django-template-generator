import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token
from django import forms

from accounts.managers import UserManager
from base.models import *


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email'), unique=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('is_staff'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'<User {self.email}>'

    @property
    def token(self):
        token, _ = Token.objects.get_or_create(user=self)
        return token

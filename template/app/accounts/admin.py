from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import *
from django.utils.translation import gettext_lazy as _


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_joined', 'created_at',)


admin.site.register(User, UserAdmin)

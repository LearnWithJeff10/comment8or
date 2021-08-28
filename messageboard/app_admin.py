# This file is named app_admin.py instead of apps.py due to a bug/change in Django 3.2+
# See https://code.djangoproject.com/ticket/32692

from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class MessageboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messageboard'

class Comment8orAdminConfig(AdminConfig):
    default_site = 'admin.Comment8orAdminSite'
from django.contrib import admin

from .models import User

# Register your models here.

# make User class have admin interface
admin.site.register(User)

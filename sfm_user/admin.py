from django.contrib import admin

from .models import User

# Register your models here.

# make User class have admin interface

class UserAdmin(admin.ModelAdmin):
    list_display = ('uid','username', 'password', 'heat', 'lastLoginDate') # list
    search_fields = ('uid', 'username', 'heat', 'lastLoginDate')

admin.site.register(User, UserAdmin)


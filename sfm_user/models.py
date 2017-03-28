from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return 'Username: ' + self.username + ' Password: ' + self.password

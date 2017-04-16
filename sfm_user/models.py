#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # 热度代表登录的频率
    heat = models.IntegerField()
    lastLoginDate = models.DateField(auto_now=True)

    def __str__(self):
        return 'Username: ' + self.username + ' Password: ' + self.password

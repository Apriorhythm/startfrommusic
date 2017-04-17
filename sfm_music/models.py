#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""


from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.

class Netease(models.Model):
    songId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    uploadDate = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return 'songId:' + self.songId + '\n title:' + self.title

class UploadFile(models.Model):
    filename = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    uploadDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'filename:' + self.filename + '\n title:' + self.title


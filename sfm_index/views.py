#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = loader.get_template('sfm_index/index.html')

    return HttpResponse(template.render(request))



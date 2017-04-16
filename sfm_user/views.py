#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User

def login(request):
    return render(request, 'sfm_user/login.html')

def register(request):
    return render(request, 'sfm_user/register.html')

@csrf_exempt
def validate(request):
    #uid = request.POST["uid"]
    #password = request.POST["password"]
    #print("uid:" + uid + "\npassword" + password)
    if request.POST:
        print("#################################")
        print(request.POST)
        print("#################################")
    return HttpResponse("OK")



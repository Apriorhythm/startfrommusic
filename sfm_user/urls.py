"""
This is user app
"""
from django.conf.urls import url
from . import views

# My Urls

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # /user/username/
    # url(r'^(?P<username>)[a-z]+$', views.fromUsernameToUid, name='fromUsernameToUid'),
]

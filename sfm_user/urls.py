from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^validate$', views.validate, name='validate'),

    # /user/username/
    # url(r'^(?P<username>)[a-z]+$', views.fromUsernameToUid, name='fromUsernameToUid'),
]

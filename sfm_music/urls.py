from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/index/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index$', views.IndexView.as_view(), name='index'),

    # /music/detail/1234/
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/netease/add/
    url(r'^netease/add$', views.NeteaseCreate.as_view(), name='netease-add'),

    # /music/netease/25/
    url(r'^netease/(?P<pk>[0-9]+)/$', views.NeteaseUpdate.as_view(),
    name='netease-update'),

    url(r'^netease/(?P<pk>[0-9]+)/delete$', views.NeteaseDelete.as_view(),
    name='netease-delete'),


]

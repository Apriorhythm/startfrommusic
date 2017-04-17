from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Netease


class IndexView(generic.ListView):
    template_name = 'sfm_music/index.html'
    context_object_name = 'all_netease'

    def get_queryset(self):
        return Netease.objects.all()


class DetailView(generic.DetailView):
    model = Netease
    template_name = 'sfm_music/detail.html'


class NeteaseCreate(CreateView):
    model = Netease
    fields = ['songId', 'title', 'artist']


class NeteaseUpdate(UpdateView):
    model = Netease
    fields = ['songId', 'title', 'artist']

class NeteaseDelete(DeleteView):
    model = Netease
    success_url = reverse_lazy('music:index')


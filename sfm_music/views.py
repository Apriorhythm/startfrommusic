from django.views import generic

from .models import Netease


class IndexView(generic.ListView):
    template_name = 'sfm_music/index.html'
    context_object_name = 'all_netease'

    def get_queryset(self):
        return Netease.objects.all()


class DetailView(generic.DetailView):
    model = Netease
    template_name = 'sfm_music/detail.html'


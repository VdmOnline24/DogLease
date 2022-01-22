import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from dgls.models import Dogs

# Create your views here.

__all__=[
    'DogsListView',
    'DogDetailView',
]



class DogsListView(ListView):
    paginate_by = 8
    model = Dogs
    template_name = 'dgls/dogs.html'

class DogDetailView(DetailView):
    queryset = Dogs.objects.all()
    template_name = 'dgls/dog_detail.html'


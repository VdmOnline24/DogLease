from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.


from crs.models import Cars

__all__=[
    'CarsListView',
    'CarDetailView',
]


class CarsListView(ListView):
    paginate_by = 11
    model = Cars
    template_name = 'crs/cars.html'

class CarDetailView(DetailView):
    queryset = Cars.objects.all()
    template_name = 'crs/car_detail.html'
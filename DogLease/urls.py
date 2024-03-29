"""DogLease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from DogLease.views import *
from dgls.views import *
from crs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepagefunc, name= 'FirstPage'),
    path('dogs/', DogsListView.as_view(), name='DogsPage'),
    path('dogs/detail/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('cars/',CarsListView.as_view(), name='cars_list'),
    path('cars/detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]

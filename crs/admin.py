from django.contrib import admin
from crs.models import Cars
# Register your models here.



class CarsAdmin(admin.ModelAdmin):

    class Meta():
        model=Cars

    list_display = [
        'crs_model',
        'crs_gosnom',
        'crs_ssp',
        'crs_sop',
        ]
    #list_editable = ['train_travel_time',]

admin.site.register(Cars, CarsAdmin)
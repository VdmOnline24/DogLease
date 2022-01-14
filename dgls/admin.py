from django.contrib import admin
from dgls.models import Dogs
# Register your models here.



class DogsAdmin(admin.ModelAdmin):

    class Meta():
        model=Dogs

    list_display = [
        'dl_code',
        'dl_status',
        'dl_vsp',
        'dl_number',
        ]
    #list_editable = ['train_travel_time',]

admin.site.register(Dogs, DogsAdmin)
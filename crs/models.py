import datetime
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.



def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Cars(models.Model):
    # DB description
    crs_model=models.CharField( null=True, blank=True, max_length=33,unique=False,verbose_name='Модель')
    crs_gosnom=models.CharField( null=True, blank=True, max_length=9,unique=False,verbose_name='Госномер')
    crs_year=models.PositiveIntegerField(default=current_year(),validators=[MinValueValidator(2001), max_value_current_year], verbose_name='Год выпуска')
    crs_vin=models.CharField(null=False,blank=False, max_length=17, verbose_name='VIN')
    crs_drive_21=models.PositiveIntegerField(null=False,blank=False, default=0, verbose_name='Пробег 2021')
    crs_drive_22 = models.PositiveIntegerField(null=False,blank=False, default=0, verbose_name='Пробег 2022')
    crs_odo_01_km = models.PositiveIntegerField(null=False,blank=False, default=0, verbose_name='Показание одометра №1')
    crs_odo_01_date = models.DecimalField(null=True,blank=True, max_length=11, max_digits=11, decimal_places=2, verbose_name='Площадь кв.м.')
    crs_ssp = models.CharField( null=True, blank=True, max_length=512, unique=False,verbose_name='ССП')
    crs_sop = models.CharField(null=True, blank=True, max_length=512, unique=False, verbose_name='Ответственный пользователь')
    crs_note = models.TextField(null=True, blank=True, unique=False, verbose_name='Заметки')



    def __str__(self):
        return f'Автомобиль {self.crs_model} , госномер {self.crs_gosnom}'


    class Meta:
        verbose_name='Автомобиль'
        verbose_name_plural='Автомобили'
        ordering=['crs_year']

    def get_absolute_url(self):
        return reverse('crs:detail', kwargs={'pk': self.pk})


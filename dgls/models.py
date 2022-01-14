from django.db import models
from django.urls import reverse
# Create your models here.



class Dogs(models.Model):
    # DB description
    dl_code=models.CharField( null=True, blank=True, max_length=8,unique=True,verbose_name='Код договора')
    dl_status=models.BooleanField(null=True,blank=True, default=True, verbose_name='Статус активности')
    dl_vsp=models.CharField(null=True,blank=True, max_length=8,unique=False,verbose_name='Код ВСП')
    dl_number=models.CharField(null=True,blank=True, max_length=128, verbose_name='Номер договора')
    dl_clnt=models.CharField(null=True,blank=True, max_length=512, verbose_name='Контрагент')
    dl_address = models.CharField(null=True,blank=True, max_length=512, verbose_name='Адрес')
    dl_type = models.CharField( null=True,blank=True, max_length=32, verbose_name='Тип договора')
    dl_sqm = models.DecimalField(null=True,blank=True, max_length=11, max_digits=11, decimal_places=2, verbose_name='Площадь кв.м.')
    #dl_sqm = models.CharField(blank=True, max_length=128, verbose_name='Площадь кв.м.')
    dl_prc_persqm=models.DecimalField(null=True,blank=True, max_length=11, max_digits=11,decimal_places=2, verbose_name='Цена за кв.м.')
    dl_prc_permnt = models.DecimalField(null=True,blank=True, max_length=11,max_digits=11, decimal_places=2, verbose_name='Цена в месяц')
    dl_dt_start=models.DateField(null=True,blank=True, verbose_name='Дата начала')
    dl_dt_finish = models.DateField(null=True,blank=True, verbose_name='Дата завершения')
    dl_dt_lastmod=models.DateField(null=True,blank=True, auto_now=True, verbose_name='Дата модификации')
    dl_note=models.TextField(null=True,blank=True, verbose_name='Заметки')


    def __str__(self):
        return f'Офис №{self.dl_vsp} , договор {self.dl_number}'


    class Meta:
        verbose_name='Договор аренды'
        verbose_name_plural='Договоры аренды'
        ordering=['dl_vsp']

    def get_absolute_url(self):
        return reverse('dgls:detail', kwargs={'pk': self.pk})

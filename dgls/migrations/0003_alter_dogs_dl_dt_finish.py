# Generated by Django 4.0.1 on 2022-01-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgls', '0002_alter_dogs_dl_address_alter_dogs_dl_clnt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='dl_dt_finish',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения'),
        ),
    ]

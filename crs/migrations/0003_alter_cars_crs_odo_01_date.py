# Generated by Django 4.0.1 on 2022-01-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crs', '0002_alter_cars_crs_drive_21_alter_cars_crs_drive_22_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='crs_odo_01_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата одометража 1'),
        ),
    ]

# Generated by Django 2.0.3 on 2018-03-18 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0010_auto_20180317_2040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='race_data',
            new_name='RaceData',
        ),
        migrations.AlterModelTable(
            name='racedata',
            table='prediction_race_data',
        ),
    ]

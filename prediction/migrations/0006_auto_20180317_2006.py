# Generated by Django 2.0.3 on 2018-03-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0005_auto_20180317_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race_data',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]

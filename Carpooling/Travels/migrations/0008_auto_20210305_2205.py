# Generated by Django 3.1.7 on 2021-03-05 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travels', '0007_auto_20210305_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travels',
            name='Passenger1',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='Passenger2',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='Passenger3',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='Passenger4',
        ),
    ]
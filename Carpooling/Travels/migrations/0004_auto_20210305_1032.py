# Generated by Django 3.1.7 on 2021-03-05 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Travels', '0003_travels_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-22 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='imageUrl',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
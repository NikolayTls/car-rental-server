# Generated by Django 4.0.6 on 2022-07-24 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_reservation_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pickup_city', to='base.city'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='city1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='return_city', to='base.city'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pickup_station', to='base.station'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='station1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='return_station', to='base.station'),
        ),
    ]

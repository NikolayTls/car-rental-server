# Generated by Django 4.0.6 on 2022-07-22 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category'),
        ),
    ]

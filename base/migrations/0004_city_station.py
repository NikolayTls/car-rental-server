# Generated by Django 4.0.6 on 2022-07-22 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_car_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('post_code', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone', models.CharField(max_length=100, null=True)),
                ('link', models.URLField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.city')),
            ],
        ),
    ]

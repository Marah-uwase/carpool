# Generated by Django 3.1.5 on 2021-01-29 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0002_delete_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Time of Journey')),
                ('cluster', models.TextField()),
                ('travel_distance', models.FloatField()),
                ('start_place', models.TextField(blank=True, verbose_name='Starting Place')),
                ('end_place', models.TextField(blank=True, verbose_name='Ending Place')),
                ('participants', models.ManyToManyField(blank=True, related_name='participants', to='carpool.CustomUser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='carpool.customuser')),
            ],
        ),
    ]

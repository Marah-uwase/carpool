# Generated by Django 3.1.5 on 2021-01-29 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0003_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_lat', models.FloatField()),
                ('start_lng', models.FloatField()),
                ('end_lat', models.FloatField()),
                ('end_lng', models.FloatField()),
                ('start_place', models.TextField(blank=True, verbose_name='Pick-up Location')),
                ('end_place', models.TextField(blank=True, verbose_name='Drop-off Location')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Declined')], max_length=20)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpool.customuser')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpool.trip')),
            ],
        ),
    ]
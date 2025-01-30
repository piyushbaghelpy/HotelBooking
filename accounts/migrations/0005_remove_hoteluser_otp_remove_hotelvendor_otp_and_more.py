# Generated by Django 5.1 on 2025-01-29 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_hoteluser_options_alter_hotelvendor_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoteluser',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='hotelvendor',
            name='otp',
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_start_date', models.DateField()),
                ('booking_end_date', models.DateField()),
                ('price', models.FloatField()),
                ('booking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hoteluser')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='accounts.hotel')),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_alter_booking_country_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='country',
            field=models.CharField(max_length=200),
        ),
    ]
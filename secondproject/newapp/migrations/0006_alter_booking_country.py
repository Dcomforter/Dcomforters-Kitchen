# Generated by Django 4.2.7 on 2023-11-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_alter_booking_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='country',
            field=models.CharField(max_length=200),
        ),
    ]

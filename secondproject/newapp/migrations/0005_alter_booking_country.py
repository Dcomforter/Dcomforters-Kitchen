# Generated by Django 4.2.7 on 2023-11-09 13:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_remove_menu_items_menu_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]

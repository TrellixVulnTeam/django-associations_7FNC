# Generated by Django 3.2.4 on 2022-07-09 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderfooditem',
            unique_together={('order', 'food_item')},
        ),
    ]

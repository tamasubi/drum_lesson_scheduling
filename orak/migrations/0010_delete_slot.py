# Generated by Django 4.2.3 on 2024-06-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orak', '0009_remove_drumlesson_date_remove_drumlesson_slot_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Slot',
        ),
    ]
# Generated by Django 4.2.3 on 2024-06-06 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orak', '0011_slot_remove_drumlesson_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='name',
        ),
    ]

# Generated by Django 4.2.3 on 2024-07-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orak', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drumlesson_option',
            name='slots',
        ),
        migrations.AddField(
            model_name='drumlesson_option',
            name='slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orak.slot', unique=True),
        ),
    ]

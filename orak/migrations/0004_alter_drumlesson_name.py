# Generated by Django 4.2.3 on 2024-06-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orak', '0003_alter_drumlesson_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drumlesson',
            name='name',
            field=models.CharField(choices=[('Élő', 'Élő'), ('Offline', 'Offline')], max_length=50),
        ),
    ]
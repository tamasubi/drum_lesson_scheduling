# Generated by Django 4.2.3 on 2024-06-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drumlesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Élő', 'Élő'), ('Online', 'Online')], max_length=50)),
                ('lesson_date', models.DateTimeField(verbose_name='Event Date')),
                ('lesson_length', models.CharField(max_length=100)),
                ('lesson_price', models.CharField(max_length=100)),
            ],
        ),
    ]
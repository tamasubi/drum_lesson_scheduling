# Generated by Django 4.2.3 on 2024-06-06 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orak', '0007_drumlesson_end_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_time', models.TimeField(null=True, verbose_name='Start Time')),
                ('end_time', models.TimeField(null=True, verbose_name='End Time')),
            ],
        ),
        migrations.RemoveField(
            model_name='drumlesson',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='drumlesson',
            name='lesson_date',
        ),
        migrations.RemoveField(
            model_name='drumlesson',
            name='lesson_length',
        ),
        migrations.RemoveField(
            model_name='drumlesson',
            name='lesson_price',
        ),
        migrations.AddField(
            model_name='drumlesson',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='drumlesson',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='drumlesson',
            name='slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orak.slot'),
        ),
    ]

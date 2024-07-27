from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.formats import date_format
from django.utils.timezone import localtime


class Slot(models.Model):
    start_time = models.TimeField('Start Time', null=True)
    end_time = models.TimeField('End Time', null=True)

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class drumlesson_option(models.Model):
    name = models.CharField(max_length=50, choices=[('Élő dobóra', 'Élő dobóra'), ('Online dobóra', 'Online dobóra')])
    date = models.DateField('Date', null=True)
    slots = models.ManyToManyField(Slot)

    def __str__(self):
       # locale.setlocale(locale.LC_TIME, 'hu_HU')
        day_of_week = date_format(self.date, 'l')
        slots_str = ', '.join([str(slot) for slot in self.slots.all()])
        return f"{self.name} - {self.date} - {day_of_week} - |{slots_str}|"

class student(AbstractUser):
    drumlessons = models.ManyToManyField(drumlesson_option, blank=True)

    def __str__(self):
        return self.username

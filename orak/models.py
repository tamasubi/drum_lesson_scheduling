from django.db import models
from django.contrib.auth.models import AbstractUser
import locale


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
        locale.setlocale(locale.LC_TIME, 'hu_HU')
        day_of_week = self.date.strftime('%A')
        slots_str = ', '.join([str(slot) for slot in self.slots.all()])
        return f"{self.name} - {self.date} - {day_of_week} - |{slots_str}|"

#class drumlesson(models.Model):
#    name = models.CharField(max_length=50, choices=[('Élő', 'Élő'), ('Offline', 'Offline')])
#    lesson_date = models.DateTimeField('Lesson Date', null=True)
#    start_time = models.TimeField('Start Time', null=True)
#    end_time = models.DateTimeField('Lesson Date', null=True)
#    lesson_length = models.CharField(max_length=100, null=True)
#    lesson_price = models.CharField(max_length=100, null=True)

#    def __str__(self):
#        locale.setlocale(locale.LC_TIME, 'hu_HU')
#        day_of_week = self.lesson_date.strftime('%A')
#        return f"{self.name} - {day_of_week} {self.lesson_date.strftime('%Y-%m-%d')} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
    

class student(AbstractUser):
    drumlesson = models.ForeignKey(drumlesson_option, blank=True, null=True, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.username



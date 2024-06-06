from django.db import models
import locale


class Slot(models.Model):
    start_time = models.TimeField('Start Time', null=True)
    end_time = models.TimeField('End Time', null=True)

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class drumlesson_option(models.Model):
    name = models.CharField(max_length=50, choices=[('Élő dobóra', 'Élő dobóra'), ('Offline dobóra', 'Offline dobóra')])
    date = models.DateField('Date', null=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True)

    def __str__(self):
        locale.setlocale(locale.LC_TIME, 'hu_HU')
        day_of_week = self.date.strftime('%A')
        return f"{self.name} - {self.date} - {day_of_week} - | {self.slot} |"

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
    
class student(models.Model):
    name = models.CharField('Student name', max_length=50)
    email_address = models.EmailField(max_length=120)
    drumlesson = models.ForeignKey(drumlesson_option, blank=True, null=True, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name
    




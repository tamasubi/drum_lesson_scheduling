from django.contrib import admin
from .models import drumlesson_option
from .models import student
from .models import Slot


admin.site.register(drumlesson_option)
admin.site.register(student)
admin.site.register(Slot)
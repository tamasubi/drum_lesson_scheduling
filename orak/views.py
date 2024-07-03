from django.shortcuts import render
from .models import drumlesson_option, student


def dates(request):
    date_list = drumlesson_option.objects.all().exclude(student__isnull=False)
    print(len(date_list))
    return render(request, 'orak/dates.html', {'date_list':date_list})


def home(request):
    name = "Tamás"
    return render(request, 'orak/home.html', {'name': name})



from django.shortcuts import render, redirect
from .models import drumlesson_option, student


def dates(request):
    date_list = drumlesson_option.objects.all().exclude(student__isnull=False)
    if request.method == 'POST':
        selected_date_id = request.POST.get('drumlesson_option')
        if selected_date_id is not None:
            try:
                selected_date = drumlesson_option.objects.get(id=int(selected_date_id))
                student = request.user
                student.drumlesson = selected_date
                student.save()
                return redirect('home')
            except ValueError:
                print("Invalid date selected")
                return redirect('dates')
    else:
        return render(request, 'orak/dates.html', {'date_list': date_list})


def home(request):
    name = request.user
    return render(request, 'orak/home.html', {'name': name})



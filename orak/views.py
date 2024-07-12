from django.shortcuts import render, redirect
from .models import drumlesson_option, student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def dates(request):
    # Exclude drumlesson_option objects already assigned to any student
    date_list = drumlesson_option.objects.filter(student__isnull=True)
    submitted = False
    if request.method == 'POST':
        selected_date_id = request.POST.get('drumlesson_option')
        if selected_date_id is not None:
            try:
                selected_date = drumlesson_option.objects.get(id=int(selected_date_id))
                user_student = request.user
                user_student.drumlessons.add(selected_date)
                user_student.save()
                messages.success(request, "Időpont foglalása sikeres!")
                submitted = True
                return redirect('home')
            except (ValueError, drumlesson_option.DoesNotExist):
                print("Invalid date selected")
                return redirect('dates')
    return render(request, 'orak/dates.html', {'date_list': date_list, 'submitted': submitted})

def home(request):
    name = request.user
    return render(request, 'orak/home.html', {'name': name})

@login_required(login_url='login')  # Ensure user is logged in to access lessons
def lessons(request):
    user_student = request.user
    drumlessons = user_student.drumlessons.all()  # Get all drum lessons related to the user
    return render(request, 'orak/lessons.html', {'drumlessons': drumlessons})


from django.shortcuts import render

def home(request):
    name = "Tamás"
    return render(request, 'orak/home.html', {'name': name})



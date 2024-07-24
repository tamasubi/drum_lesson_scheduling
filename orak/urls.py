from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('dates', views.dates, name="dates-list"),
    path('lessons', views.lessons, name='lessons'),
]
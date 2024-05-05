from django.urls import path
from . import views

path('profile/', views.profile, name='profile'),
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_unterlagen/', views.add_unterlagen, name='add_unterlagen'),
    path('add_prufung/', views.add_prufung, name='add_prufung'),
    path('add_interessante/', views.add_interessante, name='add_interessante'),
    path('add_umzug/', views.add_umzug, name='add_umzug'),
]

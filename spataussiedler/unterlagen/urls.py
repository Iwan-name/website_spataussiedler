from django.urls import path

from . import views

urlpatterns = [
    path('', views.unterlagen, name='unterlagen')
]

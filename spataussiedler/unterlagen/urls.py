from django.urls import path

from . import views

urlpatterns = [
    path('/posts', views.unterlagen, name='unterlagen'),
    path('/posts/<int:post_id>/', views.unterlagen_post_detail, name='unterlagen_post_detail')
]

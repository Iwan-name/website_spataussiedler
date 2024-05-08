from django.urls import path

from . import views
from .views import download_file

urlpatterns = [
    path('/posts', views.unterlagen, name='unterlagen'),
    path('/posts/<int:post_id>/', views.unterlagen_post_detail, name='unterlagen_post_detail'),
    path('/download/<str:file_path>/', download_file, name='download_file'),
]

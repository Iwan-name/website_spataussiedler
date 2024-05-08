import os

from django.http import FileResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from spataussiedler.settings import MEDIA_ROOT

from .models import UnterlagenModel


def unterlagen(request):
    """ Представление для страницы unterlagen(посты про документы) """
    template = 'unterlagen/unterlagen.html'
    posts = UnterlagenModel.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def unterlagen_post_detail(request, post_id):
    """ Представление для отдельного поста про документы """
    post = get_object_or_404(UnterlagenModel, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'unterlagen/unterlagen_post_detail.html', context)


def download_file(request, file_path):
    """ Функция для скачивания файлов из поста """
    print(1)
    file_path = os.path.join(MEDIA_ROOT, file_path)
    print('sss', file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse('Файла нет', status=404)

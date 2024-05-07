from django.shortcuts import render, get_object_or_404

from .models import UnterlagenModel


def unterlagen(request):
    """ Функция для страницы unterlagen(посты про документы) """
    template = 'unterlagen/unterlagen.html'
    posts = UnterlagenModel.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def unterlagen_post_detail(request, post_id):
    post = get_object_or_404(UnterlagenModel, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'unterlagen/unterlagen_post_detail.html', context)
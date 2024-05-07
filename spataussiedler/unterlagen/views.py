from django.shortcuts import render, get_object_or_404

from .models import UnterlagenModel


def unterlagen(request):
    """ Функция для страницы unterlagen(посты про документы) """
    template = 'unterlagen/unterlagen.html'
    papiers = UnterlagenModel.objects.all()
    context = {
        'papiers': papiers,
    }
    return render(request, template, context)


def unterlagen_post_detail(request, pk):
    post = get_object_or_404(UnterlagenModel, pk)
    context = {
        'post': post,
    }
    return render(request, 'unterlagen/unterlagen_post_detail.html', context)
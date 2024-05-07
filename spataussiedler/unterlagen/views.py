from django.shortcuts import render

from .models import UnterlagenModel


def unterlagen(request):
    """ Функция для страницы unterlagen(посты про документы) """
    template = 'unterlagen/unterlagen.html'
    papiers = UnterlagenModel.objects.all()
    context = {
        'papiers': papiers,
    }
    return render(request, template, context)

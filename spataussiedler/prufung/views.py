from django.shortcuts import render

from .models import PrufungModels


def prufung(request):
    """ Функция для страницы prufung(посты про экзамен) """
    template = 'prufung/prufung.html'
    examens = PrufungModels.objects.all()
    context = {
        'examens': examens,
    }
    return render(request, template, context)

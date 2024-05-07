from django.shortcuts import render
from .models import UmzugModels


def umzug(request):
    """ Функция для вывода постов про переезд """
    template = 'umzug/umzug.html'
    umzugen = UmzugModels.objects.all()
    context = {
        'umzugen': umzugen,
    }
    return render(request, template, context)

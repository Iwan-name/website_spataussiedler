from django.shortcuts import render

from .models import InteressanteOrte


def interessante(request):
    """ Функция вывода постов про интересные места """
    template = 'interessante/interessante.html'
    orte = InteressanteOrte.objects.all()
    context = {
        'orte': orte
    }
    return render(request, template, context)

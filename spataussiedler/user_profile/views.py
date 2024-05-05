from django.shortcuts import render

from interessante.models import InteressanteOrte
from prufung.models import PrufungModels
from unterlagen.models import UnterlagenModel


def profile(request):
    """ Функия прфиля пользывателя """
    template = 'user_profile/user_profile.html'
    orte = InteressanteOrte.objects.all()
    papiers = UnterlagenModel.objects.all()
    examens = PrufungModels.objects.all()
    context = {
        'orte': orte,
        'papiers': papiers,
        'examens': examens,
    }
    return render(request, template, context)


def add_unterlagen(request):
    """ Функция добавления поста про документы """
    template = 'user_profile/add_unterlagen.html'
    context = {

    }
    return render(request, template)


def add_prufung(request):
    """ Функция добавления поста про экзамен """
    template = 'user_profile/add_prufung.html'
    context = {

    }
    return render(request, template)


def add_interessante(request):
    """ Функция добавления поста про интересные места """
    template = 'user_profile/add_interessante.html'
    context = {

    }
    return render(request, template)


def add_umzug(request):
    """ Функция добавления поста про переезд """
    template = 'user_profile/add_umzug.html'
    context = {

    }
    return render(request, template)

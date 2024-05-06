from django.shortcuts import render


from prufung.models import PrufungModels
from unterlagen.models import UnterlagenModel

from interessante.models import InteressanteOrte

from .forms import UnterlagenForm

from .forms import PrufungForm


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
    form = UnterlagenForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            unterlag = form.save(commit=False)
            unterlag.autor = request.user
            unterlag.save()
            return render(request, template, context)
    else:
        form = UnterlagenForm()
    return render(request, template)


def add_prufung(request):
    """ Функция добавления поста про экзамен """
    template = 'user_profile/add_prufung.html'
    form = PrufungForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    if request.metod == 'POST':
        if form.is_valid():
            pruf = form.save(commit=False)
            pruf.author = request.user
            pruf.save()
            return render(request, template, context)
    else:
        form = PrufungForm()
    return render(request, template, context)


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

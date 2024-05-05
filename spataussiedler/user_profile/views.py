from django.shortcuts import render


def profile(request):
    """ Функия прфиля пользывателя """
    template = 'users/profile.html'
    context = {

    }
    return render(request, template)

from django.shortcuts import render


def prufung(request):
    template = 'prufung/prufung.html'
    return render(request, template)

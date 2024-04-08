from django.shortcuts import render


def unterlagen(request):
    template = 'unterlagen/unterlagen.html'
    return render(request, template)

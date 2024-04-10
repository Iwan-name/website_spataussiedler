from django.shortcuts import render


def interessante(request):
    template = 'interessante/interessante.html'
    return render(request, template)

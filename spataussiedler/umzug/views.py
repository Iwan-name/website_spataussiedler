from django.shortcuts import render


def umzug(request):
    template = 'umzug/umzug.html'
    return render(request, template)

from django.shortcuts import render


def kontakte(request):
    template = 'kontakte/kontakte.html'
    return render(request, template)
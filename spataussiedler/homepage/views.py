from django.shortcuts import render

from interessante.models import InteressanteOrte


# Create your views here.
def index(request):
    template = 'homepage/index.html'
    orte = InteressanteOrte.objects.all()
    context = {
        'orte': orte
    }
    return render(request, template, context)

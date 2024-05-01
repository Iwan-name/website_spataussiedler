from django.shortcuts import render

from .forms import InteressanteHinzufugenForm
from .models import InteressanteOrte


def interessante(request):
    template = 'interessante/interessante.html'
    orte = InteressanteOrte.objects.all()
    context = {
        'orte': orte
    }
    if request.method == 'POST':
        form = InteressanteHinzufugenForm(request.POST, request.FILES)
        if form.is_valid():
            interessante = form.save(commit=False)
            interessante.autor = request.user
            interessante.save()
            return render(request, template, {'form': form})
    else:
        form = InteressanteHinzufugenForm()
    return render(request, template, context)

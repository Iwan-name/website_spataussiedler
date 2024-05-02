from django.shortcuts import render

from .forms import UnterlagenForm
from .models import UnterlagenModel


def unterlagen(request):
    template = 'unterlagen/unterlagen.html'
    papiers = UnterlagenModel.objects.all()
    form = UnterlagenForm(request.POST, request.FILES)
    context = {
        'papiers': papiers,
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
    return render(request, template, context)

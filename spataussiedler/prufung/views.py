from django.shortcuts import render
from .models import PrufungModels
from .forms import PrufungForm


def prufung(request):
    """ Функция для страницы prufung(посты про экзамен) """
    template = 'prufung/prufung.html'
    examens = PrufungModels.objects.all()
    # form = PrufungForm(request.POST, request.FILES)
    context = {
        'examens': examens,
        # 'form': form
    }
    # if request.method == 'POST':
    #     if form.is_valid():
    #         pruf = form.save(commit=False)
    #         pruf.autor = request.user
    #         pruf.save()
    #         return render(request, template, context)
    # else:
    #     form = PrufungForm()
    return render(request, template, context)

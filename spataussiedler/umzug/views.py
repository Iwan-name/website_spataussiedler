from django.shortcuts import render


def umzug(request):
    """ Функция для вывода постов про переезд """
    template = 'umzug/umzug.html'
    return render(request, template)

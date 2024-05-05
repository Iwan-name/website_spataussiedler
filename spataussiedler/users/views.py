from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    """ Функция регистрации на сайте """
    form = SignUpForm()
    context = {
        'form': form,
    }
    template = 'users/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')

        return render(request, 'users/signup.html', {'form': form})
    return render(request, template, context)


def user_login(request):
    """ Функция для входа в учетную запись """
    tit = 'Вход на сайт'
    template = 'users/login.html'
    context = {
        'tit': tit,
        'error': 'Неверные учетные данные',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'users/login.html', context)
    else:
        return render(request, template, context)


def logout_view(request):
    """ Функция выхода из учетной записи """
    logout(request)
    return redirect('logout_page')


def logout_page(request):
    """ Функция отрисовки шаблона logout.html после выхода из учетной записи"""
    template = 'users/logout.html'
    return render(request, template)




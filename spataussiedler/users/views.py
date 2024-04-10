from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm, LoginUserForm


def signup(request):
    tit = 'Регестрация'
    context = {
        'tit': tit,
    }
    template = 'users/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            form.save()
            return redirect('index')

        form = SignUpForm()
        context = {
            'tit': tit,
            'form': form,
        }
        return render(request, 'users/signup.html', context)
    return render(request, template, context)


def user_login(request):
    tit = 'Вход на сайт'
    template = 'users/login.html'
    context = {
        'tit': tit,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Неверные учетные данные'})

    else:
        return render(request, template, context)


def logout_view(request):
    logout(request)


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import LoginForm, SignUpForm


def signup(request):
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
            # username = form.cleaned_data.get('username')
            # password1 = form.cleaned_data.get('password1')
            user.save()
            login(request, user)
            return redirect('index')

        return render(request, 'users/signup.html', {'form': form})
    return render(request, template, context)


def user_login(request):
    tit = 'Вход на сайт'

    template = 'users/login.html'
    context = {
        'tit': tit,
    }
    if request.method == 'POST':
        print(1)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.user.username)
        if user is not None:
            print(2)
            login(request, user)
            return redirect('index')
        else:
            print(3)
            return render(request, 'users/login.html', {'error': 'Неверные учетные данные'})

    else:
        print(4)
        return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('logout_page')


def logout_page(request):
    template = 'users/logout.html'
    return render(request, template)

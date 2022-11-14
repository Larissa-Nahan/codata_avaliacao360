from django.shortcuts import render, redirect
from django.http import HttpResponse
from recursos_humanos.models import Usuario
from .models import Login
from .forms import LoginForm, RecuperarSenhaForm


def login(request):
    # status = request.GET.get('status')
    form = LoginForm(request.POST or None)
    return render(request, 'login/login.html', {'form': form})

def recuperar_senha(request):
    form = RecuperarSenhaForm(request.POST or None)
    return render(request, 'login/recuperar_senha.html', {'form': form})



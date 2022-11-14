from django.shortcuts import render, redirect
from django.http import HttpResponse
from recursos_humanos.models import Usuario
from .forms import LoginForm


def login(request):
    # status = request.GET.get('status')
    form = LoginForm(request.POST or None)
    return render(request, 'login/login.html', {'form': form})



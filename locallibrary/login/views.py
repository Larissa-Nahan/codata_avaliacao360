from django.shortcuts import render, redirect
from django.http import HttpResponse
from recursos_humanos.models import Usuario
from .forms import LoginForm


def login(request):
    return render(request, 'login.html')

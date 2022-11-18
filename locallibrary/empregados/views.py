from django.shortcuts import render, redirect
from recursos_humanos.models import Usuario
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, "home_usuarios.html")

def auto(request):
    return render(request, 'empregados/auto.html')
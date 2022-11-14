from django.shortcuts import render, redirect
from django.http import HttpResponse
from recursos_humanos.models import Usuario
from .models import Login
from .forms import LoginForm, RecuperarSenhaForm


def login(request):
    status = request.GET.get('status')
    form = LoginForm(request.POST or None)
    return render(request, 'login/login.html', {'form': form, "status": status})

def validar_login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(cpf = cpf).filter(senha = senha)

        if len(usuario) == 0:
            return redirect(f'/?status=0')
        else:
            request.session['usuario'] = usuario[0].id

            if usuario[0].funcao == 'recursos_humanos':
                return redirect(f'/recursos_humanos/')
            # elif usuario[0].funcao == 'chefe':
            #     return redirect(f'/chefe/home')
            # elif usuario[0].funcao == 'gerente':
            #     return redirect(f'/gerente/home')
            # elif usuario[0].funcao == 'empregados':
            #     return redirect(f'/empregado/home')                
    else:
        return HttpResponse(f'/?status=0')
    
    return redirect(f'/?status=0')

def recuperar_senha(request):
    status = request.GET.get('status')
    form = RecuperarSenhaForm(request.POST or None)
    return render(request, 'login/recuperar_senha.html', {'form': form, "status": status})

def validar_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        usuario = Usuario.objects.filter(email = email)
        print(f'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa{usuario}')

        if len(usuario) == 0:
            print(f'Usuario nao existe')
            return redirect(f'/recuperar_senha/?status=0')
        else:
            print(f'Usuario existe')
            return HttpResponse(f'Foi')
            # return redirect(f'/')          
    else:
        print(f'nao pegou metodo post')
        return HttpResponse(f'/?status=0')
    
    print(f'erro')
    return redirect(f'/?status=0')

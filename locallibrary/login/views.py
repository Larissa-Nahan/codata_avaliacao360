from django.shortcuts import render, redirect
from django.http import HttpResponse
from recursos_humanos.models import Usuario
from .models import Login
from .forms import LoginForm, RecuperarSenhaForm


def login(request):
    status = request.GET.get('status')
    form = LoginForm(request.POST or None)
    return render(request, 'login/login.html', {'form': form, "status": status})

def recuperar_senha(request):
    form = RecuperarSenhaForm(request.POST or None)
    return render(request, 'login/recuperar_senha.html', {'form': form})

def validar_login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(cpf = cpf).filter(senha = senha)
        form = LoginForm(request.POST)

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

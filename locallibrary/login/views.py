from django.shortcuts import render, redirect
from django.http import HttpResponse
from recursos_humanos.models import Usuario
from .models import Login
from .forms import LoginForm, RecuperarSenhaForm, NovaSenhaForm


def login(request):
    status = request.GET.get('status')
    form = LoginForm(request.POST or None)
    return render(request, 'login/login.html', {'form': form, "status": status})

def validar_login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(cpf = cpf)


        if len(usuario) == 0:
            # usuario nao existe
            return redirect(f'/?status=0')
        else:
            request.session['usuario'] = usuario[0].id

            if usuario.filter(senha = senha):
                if usuario[0].funcao == 'recursos_humanos':
                    return redirect(f'/recursos_humanos/')
                # elif usuario[0].funcao == 'chefe':
                #     return redirect(f'/chefe/home')
                # elif usuario[0].funcao == 'gerente':
                #     return redirect(f'/gerente/home')
                # elif usuario[0].funcao == 'empregados':
                #     return redirect(f'/empregado/home')                
            else:
                # usuario existe mas senha errada
                return redirect(f'/?status=1')

    else:
        # erro no metodo
        return HttpResponse(f'/?status=3')

def recuperar_senha(request):
    status = request.GET.get('status')
    form = RecuperarSenhaForm(request.POST or None)
    return render(request, 'login/recuperar_senha.html', {'form': form, "status": status})

def validar_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        usuario = Usuario.objects.filter(email = email)

        if len(usuario) == 0:
            # usuario nao existe
            return redirect(f'/recuperar_senha/?status=0')
        else:
            # usuario existe
            return redirect(f'/nova_senha/')
    else:
        # erro no metodo
        return HttpResponse(f'/?status=3')

def nova_senha(request):
    status = request.GET.get('status')
    form = NovaSenhaForm(request.POST or None)
    return render(request, 'login/nova_senha.html', {'form': form, "status": status})

def validar_nova_senha(request):
    if request.method == 'POST':
        senha = request.POST.get('senha')
        nova_senha = request.POST.get('nova_senha')

        if len(senha) < 8:
            # senha menor que 8 caracteres
            return redirect(f'/nova_senha/?status=0')
        elif senha == nova_senha:
            # senhas iguais
            return redirect(f'/?status=2')
        else:
            # senhas diferentes
            return redirect(f'/nova_senha/?status=1')
    else:
        # erro no metodo
        return HttpResponse(f'/?status=3')

from django.shortcuts import render, redirect
from .forms import CadastrarUsuarioForm, EditarUsuarioForm
from .models import Usuario
from avaliacao.models import FatorDesempenhoDemerito, FatorDesempenhoMerito
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, "recursos_humanos/home.html")

def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    return render(request, "recursos_humanos/listar_usuarios.html", {'usuarios': usuarios})

def cadastrar_usuario(request):
    form = CadastrarUsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_usuarios")
    
    return render(request, "recursos_humanos/cadastrar_usuario.html", {'form': form})

def editar_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    form = EditarUsuarioForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("listar_usuarios")

    return render(request, "recursos_humanos/editar_usuario.html", {"instance": instance, "form": form})

def deletar_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    instance.delete()
    return redirect("listar_usuarios")


def avaliacao_desempenho(request):
    usuarios = Usuario.objects.all()

    return render(request, "recursos_humanos/avaliacao_desempenho.html", {'usuarios': usuarios})

def avaliar_usuario(request, id=None):
    usuario = Usuario.objects.get(id = id) 
    demeritos = FatorDesempenhoDemerito.objects.all() 
    meritos = FatorDesempenhoMerito.objects.all() 

    return render(request, "recursos_humanos/avaliar_usuario.html", {"usuario": usuario, "demeritos": demeritos, "meritos": meritos})
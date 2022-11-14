from django.shortcuts import render, redirect
from .forms import CadastrarUsuarioForm, EditarUsuarioForm
from .models import Usuario
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

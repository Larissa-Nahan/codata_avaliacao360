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

# def editar_usuario(request, id):
#     nome = request.POST.get('nome')
#     data_atualizacao = datetime.date.now().year

#     usuario = Usuario.objects.get(id = id)
#     usuario.nome = nome
#     usuario.data_atualizacao = data_atualizacao
#     form = EditarUsuarioForm()

#     if form.is_valid():
#         form.save()
#         usuario.save()

#     return redirect("listar_usuarios")

def editar_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    usuario = Usuario.objects.get(nome = instance)
    form = EditarUsuarioForm(request.POST or None, instance=instance)
    print(f"IMPRIMINDO O ID DO USUARIO: {id}")
    print(f"IMPRIMINDO O senha DO USUARIO: {usuario}")

    if form.is_valid():
        print(f"form USUARIO: valido")
        
        instance = form.save(commit=False)
        # data_atualizacao = datetime.date.now().year
        instance.save()
        return redirect("listar_usuarios")

    print(f"form USUARIO: invalido")

    return render(request, "recursos_humanos/editar_usuario.html", {"instance": instance, "form": form})

from django.shortcuts import render, redirect
from .forms import CadastrarUsuarioForm, EditarUsuarioForm, AvaliacaoForm
from .models import Usuario, Gerencia, Diretoria
from avaliacao.models import FatorDesempenhoDemerito, FatorDesempenhoMerito
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
import datetime

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

def gerencias(request):
    data = json.loads(request.body)
    id_diretoria = data["id"]
    gerencias = Gerencia.objects.filter(diretoria__id=id_diretoria)

    return JsonResponse(list(gerencias.values("id", "gerencia")), safe=False)

def editar_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    form = EditarUsuarioForm(request.POST or None, instance=instance)
    instance.data_atualizacao_usuario = datetime.datetime.now()

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("listar_usuarios")

    return render(request, "recursos_humanos/editar_usuario.html", {"instance": instance, "form": form})

def deletar_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    instance.delete()
    return redirect("listar_usuarios")


def fator_desempenho(request):
    usuarios = Usuario.objects.all()

    return render(request, "recursos_humanos/fator_desempenho.html", {'usuarios': usuarios})

def avaliar_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    form = AvaliacaoForm(request.POST or None, instance=instance)
    instance.data_ultima_avaliacao = datetime.datetime.now()

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        return redirect("/recursos_humanos/fator_desempenho")
    
    return render(request, "recursos_humanos/avaliar_usuario.html", {"instance": instance, "form": form})

def visualizar_avaliacao_usuario(request, id=None):
    instance = get_object_or_404(Usuario, id=id)
    meritos_usuario = instance.meritos.all()
    demeritos_usuario = instance.demeritos.all()

    print(demeritos_usuario)
    
    return render(request, "recursos_humanos/visualizar_avaliacao_usuario.html", {"instance": instance, "meritos_usuario": meritos_usuario, "demeritos_usuario": demeritos_usuario})

from django.shortcuts import render, redirect
from recursos_humanos.models import Usuario
from avaliacao.models import AvaliacaoDesempenho
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, "home_usuarios.html")

def auto(request):
    # instance = get_object_or_404(Usuario, id=id)
    instance = Usuario.objects.get(id = request.session['usuario'])
    avaliacoes = AvaliacaoDesempenho.objects.all()

    return render(request, 'colaboradores/auto.html', {"instance": instance, "avaliacoes": avaliacoes})

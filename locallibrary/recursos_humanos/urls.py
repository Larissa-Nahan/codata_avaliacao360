from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:id>', views.deletar_usuario, name='deletar_usuario'),
    
    
    path('avaliacao_desempenho/', views.avaliacao_desempenho, name='avaliacao_desempenho'),
    path('avaliar_usuario/<int:id>', views.avaliar_usuario, name='avaliar_usuario'),
]

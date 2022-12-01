from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-recursos_humanos'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:id>', views.deletar_usuario, name='deletar_usuario'),
    
    path('gerencias', views.gerencias, name='gerencias'),
    
    path('fator_desempenho/', views.fator_desempenho, name='fator_desempenho'),
    path('avaliar_usuario/<int:id>', views.avaliar_usuario, name='avaliar_usuario'),
]

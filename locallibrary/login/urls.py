from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('validar_email/', views.validar_email, name='validar_email'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
    path('nova_senha/', views.nova_senha, name='nova_senha'),
    path('validar_nova_senha/', views.validar_nova_senha, name='validar_nova_senha'),
]
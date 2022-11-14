from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('recursos_humanos/', include('recursos_humanos.urls')),
    path('empregados/', include('empregados.urls')),
]

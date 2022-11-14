from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recursos_humanos/', include('recursos_humanos.urls')),
]

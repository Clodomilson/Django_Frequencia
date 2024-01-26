# frequencia/urls.py

from django.contrib import admin
from django.urls import include, path
from app_freq.views import formulario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_freq/', include('app_freq.urls')),
    path('', formulario, name='formulario'),
]

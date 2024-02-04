# frequencia/urls.py

from django.contrib import admin
from django.urls import include, path
from app_freq.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_freq/', include('app_freq.urls')),
    path('', login, name='login'),
]

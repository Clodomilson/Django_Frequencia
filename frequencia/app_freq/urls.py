from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('frequencia/', views.frequencia, name='frequencia'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
]

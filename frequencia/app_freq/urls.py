from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('frequencia/', views.frequencia, name='frequencia'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('formulario/', views.formulario, name='formulario'),
]

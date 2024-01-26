from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('frequencia/', views.frequencia, name='frequencia'),
    path('cadastro/', views.frequencia, name='cadastro'),
    path('login/', views.frequencia, name='login'),
]

# app_freq/forms.py
from django import forms
from .models import Aluno
from django.contrib import messages
from django.contrib.auth import authenticate, login

class FrequenciaForm(forms.Form):
    CURSO_CHOICES = [
    ('Programador de Sistemas', 'Programador de Sistemas'),
    ('Adm.Banco de Dados', 'Adm.Banco de Dados'),
    ('Programador Web', 'Programador Web'),
]
    matricula = forms.CharField(max_length=255)
    senha = forms.CharField(widget=forms.PasswordInput)
    curso = forms.ChoiceField(choices=CURSO_CHOICES)


class LoginForm(forms.Form):
    matricula = forms.CharField(max_length=255)
    senha = forms.CharField(widget=forms.PasswordInput)

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'senha', 'nome']

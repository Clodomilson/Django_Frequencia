# app_freq/views.py
from django.shortcuts import render, redirect
from .models import Frequencia, Aluno
from .forms import FrequenciaForm, LoginForm, AlunoForm

def formulario(request):
    form = FrequenciaForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        matricula = form.cleaned_data['matricula']
        senha = form.cleaned_data['senha']
        curso = form.cleaned_data['curso']

        aluno = Aluno.objects.filter(matricula=matricula, senha=senha).first()

        if aluno:
            # Aqui, você pode salvar a frequência do aluno com o curso escolhido
            Frequencia.objects.create(aluno=aluno, curso=curso)
            # Redirecionar para uma página de confirmação ou de volta para o formulário
        else:
            error = "Matrícula e/ou senha incorretas"

    return render(request, 'app_freq/formulario.html', {'form': form, 'error': error})

def frequencia(request):
    form = FrequenciaForm(request.POST or None)
    nome = None
    frequencias = None

    if request.method == 'POST' and form.is_valid():
        matricula = form.cleaned_data['matricula']
        curso = form.cleaned_data['curso']

        aluno = Aluno.objects.filter(matricula=matricula).first()

        if aluno:
            nome = aluno.nome
            Frequencia.objects.create(matricula=matricula, curso=curso)
            frequencias = Frequencia.objects.filter(matricula=matricula)

    # return render(request, 'app_freq/frequencia.html', {'nome': nome, 'frequencias': frequencias, 'form': form})
    return render(request, 'app_freq/formulario.html', {'form': form})


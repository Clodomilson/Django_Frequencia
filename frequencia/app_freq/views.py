# app_freq/views.py
from django.shortcuts import render, redirect
from .models import Frequencia, Aluno, Curso
from .forms import FrequenciaForm, LoginForm, AlunoForm, CursoForm

def formulario(request):
    form = LoginForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        matricula = form.cleaned_data['matricula']
        senha = form.cleaned_data['senha']

        aluno = Aluno.objects.filter(matricula=matricula, senha=senha).first()

        if aluno:
            nome = aluno.nome
            return redirect('frequencia')  # Redirecionar para a página de frequência
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

    return render(request, 'app_freq/frequencia.html', {'nome': nome, 'frequencias': frequencias, 'form': form})

def curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nome_curso = form.cleaned_data['curso']
            # Cria uma nova instância do modelo Curso e salva no banco de dados
            Curso.objects.create(nome=nome_curso)
            return redirect('alguma_url_de_sucesso')  # Redirecione para outra página após o salvamento
    else:
        form = CursoForm()

    return render(request, 'formulario.html', {'form': form})

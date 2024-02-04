# app_freq/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate  # Adicione esta linha
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.urls import reverse
from .models import Frequencia, Aluno
from .forms import FrequenciaForm, LoginForm, AlunoForm

@login_required
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

    return render(request, 'app_freq/formulario.html', {'form': form, 'error': error, 'user': request.user})

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

def cadastro(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect(reverse('login'))  # Substitua com a URL para a página de login
    else:
        form = AlunoForm()

    return render(request, 'app_freq/cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            senha = form.cleaned_data['senha']

            # Adicione instrução de impressão para verificar as credenciais
            print(f"Tentativa de login com matrícula: {matricula} e senha: {senha}")


            user = authenticate(request, username=matricula, password=senha)
            if user is not None:
                # Adicione instrução de impressão para confirmar autenticação bem-sucedida
                print(f"Usuário autenticado com sucesso: {user.username}")

                auth_login(request, user)
                return redirect('formulario')  # Substitua com a URL para registro de frequência
            else:
                # Adicione instrução de impressão para indicar falha na autenticação
                print("Falha na autenticação. Matrícula ou senha incorretas.")
                messages.error(request, 'Matrícula ou senha incorretos')
    else:
        form = LoginForm()

    return render(request, 'app_freq/login.html', {'form': form})


from django.db import models

class Aluno(models.Model):
    matricula = models.CharField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)

class Frequencia(models.Model):
    matricula = models.CharField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    curso = models.CharField(max_length=255)

class Curso(models.Model):
    nome = models.CharField(max_length=100)
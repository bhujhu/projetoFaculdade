from django.db import models

class cadastro(models.Model):
    usuario = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    senha = models.CharField(max_length=50, blank=False)
    confirmaSenha = models.CharField(max_length=50, blank=False)
    endereco = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.usuario

class autenticacao(models.Model):
    usuario = models.CharField(max_length=50, blank=False)
    senha = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.usuario
        
# Create your models here.

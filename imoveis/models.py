from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    login = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=60, null=True)
    telefone = models.CharField(max_length=14)
    foto = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    bairro = models.CharField(max_length=30, blank=False)
    quadra = models.IntegerField(blank=False)
    lado = models.CharField(max_length=30, blank=False)
    numero = models.IntegerField(blank=False)
    focos_encontrados = models.CharField(max_length=150,blank=False)
    acoes_realizadas = models.TextField(blank=False)

    def __str__(self):
        return f"{self.bairro} - {self.quadra} - {self.lado} - {self.numero}"


class Pesquisa(models.Model):
    quadra = models.CharField(max_length=100)
    lado = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.quadra} - {self.lado}'

    
    def delete(self, *args, **kwargs):
        self.acoes_realizadas = f"{self.acoes_realizadas}, Deletado"
        self.save()
        super().delete(*args, **kwargs)


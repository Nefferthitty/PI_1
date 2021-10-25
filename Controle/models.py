from django.db import models
import datetime
from django.db.models.deletion import CASCADE, DO_NOTHING

class Assessor(models.Model):
    nome_assessor = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return "%s" % (self.nome_assessor)

class Vereador(models.Model):
    nome_vereador = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.nome_vereador)
   
class Tecnico(models.Model):
    nome_tecnico = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    vereador = models.ForeignKey(Vereador, on_delete=DO_NOTHING)

    def __str__(self):
        return "%s" % (self.nome_tecnico)

class Secretaria(models.Model):
    nome_secretaria = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return "%s" % (self.nome_secretaria)

class Oficio(models.Model):
    numero_oficio = models.CharField(max_length=200)
    data_emissao = models.DateField(default=datetime.date.today)
    solicitante = models.EmailField(max_length=200)
    em_nome_de = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.numero_oficio)

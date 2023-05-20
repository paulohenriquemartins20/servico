from django.db import models

class cadastro(models.Model):

    id_tudo = models.AutoField(primary_key=True)

    nomes = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    idade = models.IntegerField()
    celular = models.TextField(max_length=255)
    funcao = models.TextField(max_length=266)
    escolaridade = models.TextField(max_length=233)
    referencias = models.TextField(max_length=233)
    estadocivil = models.TextField(max_length=233)

    




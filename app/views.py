from django.shortcuts import render

from django.http import HttpResponse

from .models import cadastro

def index(request): 
    
    mostra = cadastro()
    def tudo():
     cadastro.objects.all().delete()

    def escolherum(teste):
       cadastro.objects.filter(id_tudo=teste).delete()
    usu = {
        'usu': cadastro.objects.all(),
    }
    
    



    return render(request,'index.html',usu)

def index2(request):

    te = cadastro()


    te.nomes = request.POST.get('nomes')
    te.sobrenome = request.POST.get('sobrenome')
    te.idade = request.POST.get('idade')
    te.celular = request.POST.get('celular')
    te.funcao = request.POST.get('funcao')
    te.escolaridade = request.POST.get('escolaridade')
    te.referencias = request.POST.get('referencias')
    te.estadocivil = request.POST.get('estadocivil')
    te.save()
    g = 'nomes'
    return HttpResponse("Deu certo ")

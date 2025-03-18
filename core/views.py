from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

""" teste de push no TRAE, e teste de palavras chave em portugues"""
# Create your views here.
def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso' : 'Programar web com django',
        'outro' : 'Django é massa',
        'produto' : produtos
    }
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
#    prod = Produto.objects.get(id=pk)
    prod =get_object_or_404(Produto, id=pk)
    
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error_404(request, ex ):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500) 
 
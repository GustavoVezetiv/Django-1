from django.shortcuts import render

from .models import Produto

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
    prod = Produto.objects.get(id=pk)
    
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)
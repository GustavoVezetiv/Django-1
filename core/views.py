from django.shortcuts import render

# Create your views here.
def index(request):
    produtos = Produtos.objects.all()

    context = {
        'curso' : 'Programar web com django',
        'outro' : 'Django é massa',
        'produto' : produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)
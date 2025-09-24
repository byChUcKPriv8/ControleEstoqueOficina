from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemEstoque

def dashboard(request):
    itens = ItemEstoque.objects.all()
    return render(request, 'produtos/dashboard.html', {'itens': itens})

def entrada_estoque(request, id):
    item = get_object_or_404(ItemEstoque, id=id)
    item.quantidade += 1
    item.save()
    return redirect('dashboard')

def saida_estoque(request, id):
    item = get_object_or_404(ItemEstoque, id=id)
    if item.quantidade > 0:
        item.quantidade -= 1
        item.save()
    return redirect('dashboard')

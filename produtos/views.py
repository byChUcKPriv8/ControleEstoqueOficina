from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages

from .models import ItemEstoque
from .forms import VendaForm


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


@transaction.atomic
def criar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            item = venda.produto

            # validações de negócio
            if venda.quantidade <= 0:
                form.add_error('quantidade', 'A quantidade deve ser maior que zero.')
            elif venda.quantidade > item.quantidade:
                form.add_error(
                    'quantidade',
                    f'Estoque insuficiente. Disponível: {item.quantidade} unidade(s).'
                )
            else:
                # baixa de estoque
                item.quantidade -= venda.quantidade
                item.save()
                venda.save()
                messages.success(request, 'Venda registrada com sucesso!')
                return redirect('dashboard')
    else:
        form = VendaForm()

    return render(request, 'vendas/venda_form.html', {'form': form})

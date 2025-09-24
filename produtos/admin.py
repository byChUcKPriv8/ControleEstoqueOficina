from django.contrib import admin
from .models import ItemEstoque

@admin.register(ItemEstoque)
class ItemEstoqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_referencia', 'quantidade', 'estoque_minimo', 'fabricante')
    search_fields = ('nome', 'codigo_referencia', 'fabricante')
    list_filter = ('fabricante',)

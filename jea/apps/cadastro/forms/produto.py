# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _

from jea.apps.cadastro.models.produto import Produto, Unidade, Marca, Categoria
from jea.apps.estoque.models.local import LocalEstoque

from decimal import Decimal


class ProdutoForm(forms.ModelForm):
    custo = forms.DecimalField(max_digits=16, decimal_places=2, localize=True, widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'placeholder': 'R$ 0,00'}), initial=Decimal('0.00'), label='Custo', required=False)
    venda = forms.DecimalField(max_digits=16, decimal_places=2, localize=True, widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'placeholder': 'R$ 0,00'}), initial=Decimal('0.00'), label='Venda', required=False)

    # Estoque
    estoque_inicial = forms.DecimalField(max_digits=16, decimal_places=2, localize=True, widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask'}), label='Qtd. em estoque inicial', initial=Decimal('0.00'), required=False)
    local_dest = forms.ModelChoiceField(queryset=LocalEstoque.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}), empty_label=None, label='Localização do estoque de destino', required=False)

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['estoque_minimo'].localize = True

    class Meta:
        model = Produto
        fields = ('codigo', 'codigo_barras', 'descricao', 'categoria', 'marca', 'unidade', 'venda', 'custo', 'inf_adicionais',
                 'estoque_minimo', 'controlar_estoque',)
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_barras': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'inf_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
            'estoque_minimo': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'controlar_estoque': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'codigo': _('Código'),
            'codigo_barras': _('Código de Barras (GTIN/EAN)'),
            'descricao': _('Descrição'),
            'categoria': _('Categoria'),
            'marca': _('Marca'),
            'unidade': _('Unidade'),
            'inf_adicionais': _('Informações adicionais'),
            'estoque_minimo': _('Qtd. em estoque mínima'),
            'controlar_estoque': _('Controlar estoque deste produto?'),
        }


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('categoria_desc',)
        widgets = {
            'categoria_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'categoria_desc': _('Categoria'),
        }


class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ('marca_desc',)
        widgets = {
            'marca_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'marca_desc': _('Marca'),
        }


class UnidadeForm(forms.ModelForm):

    class Meta:
        model = Unidade
        fields = ('sigla_unidade', 'unidade_desc',)
        widgets = {
            'unidade_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla_unidade': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'unidade_desc': _('Nome descritivo'),
            'sigla_unidade': _('Sigla'),
        }
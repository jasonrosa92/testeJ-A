# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory

from jea.apps.vendas.models.vendas import PedidoVenda, ItensVenda, Venda


class VendaForm(forms.ModelForm):
    total_sem_imposto = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'readonly': True}), label='Total s/ imposto (R$)', required=False)

    def __init__(self, *args, **kwargs):
        super(VendaForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = '0'

        self.fields['total_sem_imposto'].localize = True
        self.fields['total_sem_imposto'].initial = '0.00'

        self.fields['valor_total'].localize = True
        self.fields['valor_total'].initial = '0.00'

    class Meta:
        fields = ('data_emissao', 'cliente', 'ind_final',  'vendedor', 'movimentar_estoque',
                   'valor_total', 'observacoes',)

        widgets = {
            'data_emissao': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'ind_final': forms. CheckboxInput(attrs={'class': 'form-control'}),
            'movimentar_estoque': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_total': forms.TextInput(attrs={'class': 'form-control decimal-mask', 'readonly': True}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'data_emissao': _('Data de Emissão'),
            'cliente': _('Cliente'),
            'ind_final': _('Consumidor final?'),
            'movimentar_estoque': _('Movimentar estoque?'),
            'vendedor': _('Vendedor'),
            'valor_total': _('Total (R$)'),
            'observacoes': _('Observações'),
        }


class PedidoVendaForm(VendaForm):

    class Meta(VendaForm.Meta):
        model = PedidoVenda
        fields = VendaForm.Meta.fields + \
            ('data_entrega', 'status', 'orcamento',)
        widgets = VendaForm.Meta.widgets
        widgets['data_entrega'] = forms.DateInput(
            attrs={'class': 'form-control datepicker'})
        widgets['status'] = forms.Select(
            attrs={'class': 'form-control', 'disabled': True})
        widgets['orcamento'] = forms.Select(
            attrs={'class': 'form-control', 'disabled': True})
        labels = VendaForm.Meta.labels
        labels['data_entrega'] = _('Data de Entrega')
        labels['status'] = _('Status')
        labels['orcamento'] = _('Orçamento')


class ItensVendaForm(forms.ModelForm):
    total_sem_desconto = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'readonly': True}), label='Subtotal s/ desconto', required=False)
    total_impostos = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'readonly': True}), label='Impostos', required=False)
    total_com_impostos = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'readonly': True}), label='Total', required=False)
    calculo_imposto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'hidden', 'disabled': True}), label='Cálc. Impostos', required=False)


    def __init__(self, *args, **kwargs):
        super(ItensVendaForm, self).__init__(*args, **kwargs)
        self.fields['quantidade'].localize = True
        self.fields['valor_unit'].localize = True
        self.fields['desconto'].localize = True
        self.fields['subtotal'].localize = True

        self.fields['total_sem_desconto'].localize = True

    class Meta:
        model = ItensVenda
        fields = ('produto', 'quantidade', 'valor_unit', 'tipo_desconto', 'desconto', 'valor_rateio_frete', 'valor_rateio_despesas', 'valor_rateio_seguro',
                  'vbc_icms', 'vbc_icms_st', 'vbc_ipi',
                  'subtotal')
                   
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control select-produto'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'valor_unit': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'subtotal': forms.TextInput(attrs={'class': 'form-control decimal-mask', 'readonly': True}),
            'tipo_desconto': forms.Select(attrs={'class': 'form-control'}),
            'desconto': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),


        }
        labels = {
            'produto': _('Produto'),
            'quantidade': _('Quantidade'),
            'valor_unit': _('Vl. Unit.'),
            'subtotal': _('Subtotal'),

            'tipo_desconto': _('Tipo de desconto'),
            'desconto': _('Desconto (% ou R$)'),
        }

    def is_valid(self):
        valid = super(ItensVendaForm, self).is_valid()
        if self.cleaned_data.get('produto', None) is None:
            self.cleaned_data = {}
        return valid


ItensVendaFormSet = inlineformset_factory(
    Venda, ItensVenda, form=ItensVendaForm, extra=1, can_delete=True)
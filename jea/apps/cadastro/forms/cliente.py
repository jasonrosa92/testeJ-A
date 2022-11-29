# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _

from jea.apps.cadastro.models.cliente import Cliente


class ClienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['limite_de_credito'].localize = True

    class Meta:
        model = Cliente
        fields = ('nome_razao_social', 'tipo_pessoa', 'inscricao_municipal',
                  'limite_de_credito', 'id_estrangeiro', 'informacoes_adicionais', )
        widgets = {
            'nome_razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.RadioSelect(attrs={'class': 'form-control'}),
            'limite_de_credito': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_razao_social': _('Razão Social'),
            'tipo_pessoa': _(''),
            'limite_de_credito': _('Limite de Crédito'),
            'informacoes_adicionais': _('Informações Adicionais'),
        }

    def save(self, commit=True):
        instance = super(ClienteForm, self).save(commit=False)
        instance.criado_por = self.request.user
        if commit:
            instance.save()
        return 
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

from jea.apps.cadastro.models.cliente import Cliente 
from jea.apps.cadastro.models.produto import Produto
from jea.apps.cadastro.models.empresa import Empresa
from jea.apps.vendas.models.vendas import OrcamentoVenda, PedidoVenda

from datetime import datetime


class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        quantidade_cadastro = {}
        agenda_hoje = {}
        alertas = {}
        data_atual = datetime.now().date()

        context['data_atual'] = data_atual.strftime('%d/%m/%Y')

        quantidade_cadastro['clientes'] = Cliente.objects.all().count()
        quantidade_cadastro['produtos'] = Produto.objects.all().count()
        quantidade_cadastro['empresas'] = Empresa.objects.all().count()
        agenda_hoje['orcamento_venda_hoje'] = OrcamentoVenda.objects.filter(
            data_vencimento=data_atual, status='0').count()
        agenda_hoje['pedido_venda_hoje'] = PedidoVenda.objects.filter(
            data_entrega=data_atual, status='0').count()
        context['agenda_hoje'] = agenda_hoje

        alertas['produtos_baixo_estoque'] = Produto.objects.filter(
            estoque_atual__lte=F('estoque_minimo')).count()
        alertas['orcamentos_venda_vencidos'] = OrcamentoVenda.objects.filter(
            data_vencimento__lte=data_atual, status='0').count()
        alertas['pedidos_venda_atrasados'] = PedidoVenda.objects.filter(
            data_entrega__lte=data_atual, status='0').count()

        return context

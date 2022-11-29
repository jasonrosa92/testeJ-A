# -*- coding: utf-8 -*-

from django.urls import re_path

from jea.apps.vendas.views.vendas import (AdicionarPedidoVendaView, PedidoVendaListView, EditarPedidoVendaView,
                                          PedidoVendaAtrasadosListView, PedidoVendaEntregaHojeListView,
                                          GerarCopiaPedidoVendaView, GerarPDFPedidoVenda, CancelarPedidoVendaView, GerarPedidoVendaView, GerarPDFOrcamentoVenda) 
from jea.apps.vendas.views.pagamento import AdicionarCondicaoPagamentoView, CondicaoPagamentoListView, EditarCondicaoPagamentoView, InfoCondicaoPagamento
from jea.apps.vendas.views.ajax_views import InfoVenda


app_name = 'vendas'
urlpatterns = [
    # Pedidos de venda
    # vendas/pedidovenda/adicionar/
    re_path(r'pedidovenda/adicionar/$',
        AdicionarPedidoVendaView.as_view(), name='addpedidovendaview'),
    # vendas/pedidovenda/listapedidovenda
    re_path(r'pedidovenda/listapedidovenda/$',
        PedidoVendaListView.as_view(), name='listapedidovendaview'),
    # vendas/pedidovenda/editar/
    re_path(r'pedidovenda/editar/(?P<pk>[0-9]+)/$',
        EditarPedidoVendaView.as_view(), name='editarpedidovendaview'),
    # vendas/pedidovenda/listapedidovenda/atrasados
    re_path(r'pedidovenda/listapedidovenda/atrasados/$',
        PedidoVendaAtrasadosListView.as_view(), name='listapedidovendaatrasadosview'),
    # vendas/pedidovenda/listapedidovenda/hoje
    re_path(r'pedidovenda/listapedidovenda/hoje/$',
        PedidoVendaEntregaHojeListView.as_view(), name='listapedidovendahojeview'),

    # Condicao pagamento
    # vendas/pagamento/adicionar/
    re_path(r'pagamento/adicionar/$', AdicionarCondicaoPagamentoView.as_view(),
        name='addcondicaopagamentoview'),
    # vendas/pagamento/listacondicaopagamento
    re_path(r'pagamento/listacondicaopagamento/$',
        CondicaoPagamentoListView.as_view(), name='listacondicaopagamentoview'),
    # vendas/pagamento/editar/
    re_path(r'pagamento/editar/(?P<pk>[0-9]+)/$', EditarCondicaoPagamentoView.as_view(
    ), name='editarcondicaopagamentoview'),

    # Request ajax views
    re_path(r'infocondpagamento/$', InfoCondicaoPagamento.as_view(),
        name='infocondpagamento'),
    re_path(r'infovenda/$', InfoVenda.as_view(), name='infovenda'),

    # Gerar pdf pedido
    re_path(r'gerarpdfpedidovenda/(?P<pk>[0-9]+)/$',
        GerarPDFPedidoVenda.as_view(), name='gerarpdfpedidovenda'),
    # Gerar pedido a partir de um orçamento
    re_path(r'gerarpedidovenda/(?P<pk>[0-9]+)/$',
        GerarPedidoVendaView.as_view(), name='gerarpedidovenda'),
    # Copiar orcamento cancelado ou baixado
    # Copiar pedido cancelado ou baixado
    re_path(r'copiarpedidovenda/(?P<pk>[0-9]+)/$',
        GerarCopiaPedidoVendaView.as_view(), name='copiarpedidovenda'),
    # Cancelar Pedido de venda
    re_path(r'cancelarpedidovenda/(?P<pk>[0-9]+)/$',
        CancelarPedidoVendaView.as_view(), name='cancelarpedidovenda'),]
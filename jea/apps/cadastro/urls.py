from django.urls import re_path

from jea.apps.cadastro.views.empresa import AdicionarEmpresaView,EmpresasListView, EditarEmpresaView
from jea.apps.cadastro.views.cliente import AdicionarClienteView, ClientesListView,EditarClienteView
from jea.apps.cadastro.views.produto import (AdicionarProdutoView, ProdutosListView, ProdutosBaixoEstoqueListView,
                                             EditarProdutoView, AdicionarCategoriaView, CategoriasListView, EditarCategoriaView, 
                                             AdicionarUnidadeView, UnidadesListView, EditarUnidadeView,
                                             AdicionarMarcaView, MarcasListView, EditarMarcaView)
from jea.apps.cadastro.views.ajax_views import InfoCliente, InfoEmpresa, InfoProduto

app_name = 'cadastro'
urlpatterns = [
    # Empresa
    # cadastro/empresa/adicionar/
    re_path(r'empresa/adicionar/$',
        AdicionarEmpresaView.as_view(), name='addempresaview'),
    # cadastro/empresa/listaempresas
    re_path(r'empresa/listaempresas/$',
        EmpresasListView.as_view(), name='listaempresasview'),
    # cadastro/empresa/editar/
    re_path(r'empresa/editar/(?P<pk>[0-9]+)/$',
        EditarEmpresaView.as_view(), name='editarempresaview'),

    # Cliente
    # cadastro/cliente/adicionar/
    re_path(r'cliente/adicionar/$',
        AdicionarClienteView.as_view(), name='addclienteview'),
    # cadastro/cliente/listaclientes
    re_path(r'cliente/listaclientes/$',
        ClientesListView.as_view(), name='listaclientesview'),
    # cadastro/cliente/editar/
    re_path(r'cliente/editar/(?P<pk>[0-9]+)/$',
        EditarClienteView.as_view(), name='editarclienteview'),

    # Produto
    # cadastro/produto/adicionar/
    re_path(r'produto/adicionar/$',
        AdicionarProdutoView.as_view(), name='addprodutoview'),
    # cadastro/produto/listaprodutos
    re_path(r'produto/listaprodutos/$',
        ProdutosListView.as_view(), name='listaprodutosview'),
    # cadastro/produto/listaprodutos/baixoestoque
    re_path(r'produto/listaprodutos/baixoestoque/$',
        ProdutosBaixoEstoqueListView.as_view(), name='listaprodutosbaixoestoqueview'),
    # cadastro/produto/editar/
    re_path(r'produto/editar/(?P<pk>[0-9]+)/$',
        EditarProdutoView.as_view(), name='editarprodutoview'),

    # Outros
    # Categorias
    # cadastro/outros/adicionarcategoria/
    re_path(r'outros/adicionarcategoria/$',
        AdicionarCategoriaView.as_view(), name='addcategoriaview'),
    # cadastro/outros/listacategorias/
    re_path(r'outros/listacategorias/$',
        CategoriasListView.as_view(), name='listacategoriasview'),
    # cadastro/outros/editarcategoria/
    re_path(r'outros/editarcategoria/(?P<pk>[0-9]+)/$',
        EditarCategoriaView.as_view(), name='editarcategoriaview'),

    # Unidades
    # cadastro/outros/adicionarunidade/
    re_path(r'outros/adicionarunidade/$',
        AdicionarUnidadeView.as_view(), name='addunidadeview'),
    # cadastro/outros/listaunidades/
    re_path(r'outros/listaunidades/$',
        UnidadesListView.as_view(), name='listaunidadesview'),
    # cadastro/outros/editarcunidade/
    re_path(r'outros/editarunidade/(?P<pk>[0-9]+)/$',
        EditarUnidadeView.as_view(), name='editarunidadeview'),

    # Marcas
    # cadastro/outros/adicionarmarca/
    re_path(r'outros/adicionarmarca/$',
        AdicionarMarcaView.as_view(), name='addmarcaview'),
    # cadastro/outros/listamarcas/
    re_path(r'outros/listamarcas/$',
        MarcasListView.as_view(), name='listamarcasview'),
    # cadastro/outros/editarmarca/
    re_path(r'outros/editarmarca/(?P<pk>[0-9]+)/$',
        EditarMarcaView.as_view(), name='editarmarcaview'),

    # Informacoes de dada empresa (Ajax request)
    re_path(r'infoempresa/$', InfoEmpresa.as_view(), name='infoempresa'),
    re_path(r'infocliente/$', InfoCliente.as_view(), name='infocliente'),
    re_path(r'infoproduto/$', InfoProduto.as_view(), name='infoproduto'),
]
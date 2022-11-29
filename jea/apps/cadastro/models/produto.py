# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


TP_OPERACAO_OPCOES = (
    (u'0', u'0 - Entrada'),
    (u'1', u'1 - Saída'),
)

ID_DEST_OPCOES = (
    (u'1', u'1 - Operação interna.'),
    (u'2', u'2 - Operação interestadual.'),
    (u'3', u'3 - Operação com exterior'),
)


class Categoria(models.Model):
    categoria_desc = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Categoria"

    def __unicode__(self):
        s = u'%s' % (self.categoria_desc)
        return s

    def __str__(self):
        s = u'%s' % (self.categoria_desc)
        return s


class Marca(models.Model):
    marca_desc = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Marca"

    def __unicode__(self):
        s = u'%s' % (self.marca_desc)
        return s

    def __str__(self):
        s = u'%s' % (self.marca_desc)
        return s


class Unidade(models.Model):
    sigla_unidade = models.CharField(max_length=3)
    unidade_desc = models.CharField(max_length=16)

    class Meta:
        verbose_name = "Unidade"

    def __unicode__(self):
        s = u'(%s) %s' % (self.sigla_unidade, self.unidade_desc)
        return s

    def __str__(self):
        s = u'(%s) %s' % (self.sigla_unidade, self.unidade_desc)
        return s


class Produto(models.Model):
    # Dados gerais
    codigo = models.CharField(max_length=15)
    codigo_barras = models.CharField(
        max_length=16, null=True, blank=True)  # GTIN/EAN
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.PROTECT)
    marca = models.ForeignKey(
        Marca, null=True, blank=True, on_delete=models.PROTECT)
    unidade = models.ForeignKey(
        Unidade, null=True, blank=True, on_delete=models.PROTECT)
    custo = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    venda = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    # Estoque
    estoque_minimo = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                         MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    estoque_atual = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                        MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    controlar_estoque = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"

    @property
    def format_unidade(self):
        if self.unidade:
            return self.unidade.sigla_unidade
        else:
            return ''

    def get_sigla_unidade(self):
        if self.unidade:
            return self.unidade.sigla_unidade
        else:
            return ''

    def get_cfop_padrao(self):
        if self.cfop_padrao:
            return self.cfop_padrao.cfop
        else:
            return ''

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s
# -*- coding: utf-8 -*-

from django.db import models

from decimal import Decimal

from jea.apps.cadastro.models.base import Pessoa


class Cliente(Pessoa):
    limite_de_credito = models.DecimalField(
        max_digits=15, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    id_estrangeiro = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
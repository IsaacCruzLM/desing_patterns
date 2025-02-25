import random
from django.db import models
from abc import ABCMeta, abstractmethod

# Create your models here.

class Gateway:
    def cobrar(self) -> bool:
        return random.choice([True, False])

class PagamentoMeta(ABCMeta, type(models.Model)):
    pass

class Pagamento(models.Model, metaclass=PagamentoMeta):
    valor = models.FloatField()

    class Meta:
        abstract = True  # Django não cria uma tabela para esta classe
    
    def __init__(self, *args, gateway_cls=Gateway, **kwargs):
        super().__init__(*args, **kwargs)
        self.gateway = gateway_cls()  # Instancia a classe de gateway

    @abstractmethod
    def calcular_desconto(self) -> float:
        """Cada tipo de pagamento implementará seu próprio calculo"""
        pass

    def calcular_taxa(self) -> float:
        return 0
    
    def realiza_cobranca(self) -> bool:
        valor_final = self.valor + self.calcular_taxa() - self.calcular_desconto()
        was_paid = "Pagamento realizado" if self.gateway.cobrar() else "Pagamento não realizado"
        return f"{self.valor} + {self.calcular_taxa()} - {self.calcular_desconto()} = {valor_final} -> {was_paid}"

class PagamentoCredito(Pagamento):
    def calcular_taxa(self) -> float:
        return self.valor * 0.05
    
    def calcular_desconto(self) -> float:
        if(self.valor > 300):
            return self.valor * 0.02
        return 0

class PagamentoDebito(Pagamento):
    def calcular_taxa(self) -> float:
        return 4
    
    def calcular_desconto(self) -> float:
        return self.valor * 0.05

class PagamentoDinheiro(Pagamento):
    def calcular_desconto(self) -> float:
        return self.valor * 0.1
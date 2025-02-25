from abc import ABCMeta, abstractmethod
from django.db import models

from .strategies.base import EstrategiaFrete

class PedidoMeta(ABCMeta, type(models.Model)):
    pass

class Pedido(models.Model, metaclass=PedidoMeta):
    """Classe abstrata que representa um pedido no banco de dados"""
    nome_cliente = models.CharField(max_length=255)
    nome_produto = models.CharField(max_length=255)
    valor = models.FloatField()

    class Meta:
        abstract = True  # Django não cria uma tabela para esta classe

    def __init__(self, *args, frete: EstrategiaFrete, **kwargs):
        super().__init__(*args, **kwargs)
        self.frete = frete

    @abstractmethod
    def processar_pedido(self):
        """Cada tipo de pedido implementará seu próprio processamento"""
        pass

    def calcular_frete(self) -> float:
        return self.frete.calcular_frete(self.valor)
  
class PedidoEletronica(Pedido):
    categoria = "Eletrônicos"

    def processar_pedido(self):
        return f"Processando pedido do produto {self.nome_produto} da categoria {self.categoria} para {self.nome_cliente}"

class PedidoMoveis(Pedido):
    categoria = "Móveis"

    def processar_pedido(self):
        return f"Processando pedido do produto {self.nome_produto} da categoria {self.categoria} para {self.nome_cliente}"
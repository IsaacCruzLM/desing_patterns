from django.db import models
from abc import ABC, abstractmethod

## Interfaces
class Gateway(ABC):
    @abstractmethod
    def set_valor(self, valor: float):
        pass
    
    @abstractmethod
    def set_parcelas(self, parcelas: int):
        pass
    
    @abstractmethod
    def set_numero_cartao(self, numero_cartao: str):
        pass
    
    @abstractmethod
    def set_cvv(self, cvv: str):
        pass
    
    @abstractmethod
    def validar_cartao(self) -> bool:
        pass

    @abstractmethod
    def realizar_pagamento(self) -> bool:
        pass

## Classe de Gateway de pagamentos (Classes de Terceiros)
class TopPagamentos():
    def __init__(self):
        self.valor = 0.0
        self.parcelas = 0
        self.numero_cartao = ""
        self.cvv = ""
  
    def set_valor_total(self, valor: float):
        self.valor = valor
    
    def set_quantidade_parcelas(self, parcelas: int):
        self.parcelas = parcelas
    
    def set_cartao(self, numero_cartao: str, cvv: str):
        self.numero_cartao = numero_cartao
        self.cvv = cvv

    def realizar_pagamento(self) -> bool:
        print("Pagamento Realizado via Top Pagamentos")
        return True

class PagFacil():
    def __init__(self):
        self.valor = 0.0
        self.parcelas = 0
        self.numero_cartao = ""
        self.cvv = ""
  
    def set_valor(self, valor: float):
        self.valor = valor
    
    def set_parcelas(self, parcelas: int):
        self.parcelas = parcelas
    
    def set_numero_cartao(self, numero_cartao: str):
        self.numero_cartao = numero_cartao
    
    def set_cvv(self, cvv: str):
        self.cvv = cvv
    
    def validar_cartao(self) -> bool:
        if(self.numero_cartao != "" and self.cvv != "" and len(self.cvv) == 3):
            return True
        return False

    def realizar_pagamento(self) -> bool:
        print("Pagamento Realizado via PagFácil")
        return True

## Adpters
class PagFacilAdapter(PagFacil, Gateway):
    pass

class TopPagamentosAdapter(Gateway):
    def __init__(self, top_pagamentos: TopPagamentos):
        self.TopPagamentos = top_pagamentos
        self.cvv = None
        self.numero_cartao = None
    
    def set_valor(self, valor: float):
        self.TopPagamentos.set_valor_total(valor)
    
    def set_parcelas(self, parcelas: int):
        self.TopPagamentos.set_quantidade_parcelas(parcelas)
    
    def set_numero_cartao(self, numero_cartao: str):
        self.numero_cartao = numero_cartao

        if(self.cvv != None):
            self.TopPagamentos.set_cartao(numero_cartao=self.numero_cartao, cvv=self.cvv)
    
    def set_cvv(self, cvv: str):
        self.cvv = cvv

        if(self.numero_cartao != None):
            self.TopPagamentos.set_cartao(numero_cartao=self.numero_cartao, cvv=self.cvv)
    
    def validar_cartao(self) -> bool:
        return True

    def realizar_pagamento(self) -> bool:
        return self.TopPagamentos.realizar_pagamento()

class Cobranca():
    def __init__(self, gateway: Gateway):
        self.Gateway = gateway
        self.parcelas = 0
        self.numero_cartao = ""
        self.cvv = ""
  
    def set_gateway(self, gateway: Gateway):
        self.Gateway = gateway
    
    def set_valor(self, valor: float):
        self.Gateway.set_valor(valor)
    
    def set_parcelas(self, parcelas: int):
        self.parcelas = parcelas
    
    def set_numero_cartao(self, numero_cartao: str):
        self.numero_cartao = numero_cartao
    
    def set_cvv(self, cvv: str):
        self.cvv = cvv
    
    def validar_cartao(self) -> bool:
        if(self.numero_cartao != "" and self.cvv != "" and len(self.cvv) == 3):
            return True
        return False

    def realizar_pagamento(self) -> bool:
        print("Pagamento Realizado via PagFácil")
        return True


            
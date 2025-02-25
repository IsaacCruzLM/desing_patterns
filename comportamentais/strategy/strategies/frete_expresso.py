from .base import EstrategiaFrete

class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, valor: float) -> float:
        return valor * 0.1
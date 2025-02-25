from .base import EstrategiaFrete

class FreteComum(EstrategiaFrete):
    def calcular_frete(self, valor: float) -> float:
        return valor * 0.05
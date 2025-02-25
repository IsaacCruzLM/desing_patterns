from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    """Interface para estratégias de frete"""
    
    @abstractmethod
    def calcular_frete(self, valor: float) -> float:
        """Calcula o frete com base no valor"""
        pass
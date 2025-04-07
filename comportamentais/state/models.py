from abc import ABC, abstractmethod
# Create your models here.

class State(ABC):
    def sucesso_ao_pagar(self):
        pass

    def cancelar_pedido(self):
        pass

    def despachar_pedido(self):
        pass

class AguardandoPagamentoState(State):
    def __init__(self, pedido):
        self.pedido = pedido

    def sucesso_ao_pagar(self):
        self.pedido.set_estado_atual(self.pedido.pago)

    def cancelar_pedido(self):
        self.pedido.set_estado_atual(self.pedido.cancelado)

    def despachar_pedido(self):
        raise NotImplementedError("Operação não suportada, o pedido ainda não foi pago")

class PagoState(State):
    def __init__(self, pedido):
        self.pedido = pedido

    def sucesso_ao_pagar(self):
        raise NotImplementedError("Operação não suportada, o pedido já foi pago")

    def cancelar_pedido(self):
        self.pedido.set_estado_atual(self.pedido.cancelado)

    def despachar_pedido(self):
        self.pedido.set_estado_atual(self.pedido.enviado)

class CanceladoState(State):
    def __init__(self, pedido):
        self.pedido = pedido

    def sucesso_ao_pagar(self):
        raise NotImplementedError("Operação não suportada, o pedido se encontra cancelado")

    def cancelar_pedido(self):
        raise NotImplementedError("Operação não suportada, o pedido já foi cancelado")

    def despachar_pedido(self):
        raise NotImplementedError("Operação não suportada, o pedido se encontra cancelado")

class EnviadoState(State):
    def __init__(self, pedido):
        self.pedido = pedido

    def sucesso_ao_pagar(self):
        raise NotImplementedError("Operação não suportada, o pedido já foi pago e enviado")

    def cancelar_pedido(self):
        raise NotImplementedError("Operação não suportada, o pedido já foi enviado")

    def despachar_pedido(self):
        raise NotImplementedError("Operação não suportada, o pedido já foi enviado")


class Pedido():
    aguardando_pagamento: State
    pago: State
    cancelado: State
    enviado: State
    estado_atual: State

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aguardando_pagamento = AguardandoPagamentoState(pedido=self)
        self.pago = PagoState(pedido=self)
        self.cancelado = CanceladoState(pedido=self)
        self.enviado = EnviadoState(pedido=self)
        self.estado_atual = self.aguardando_pagamento

    def realizar_pagamento(self):
        try:
            self.estado_atual.sucesso_ao_pagar()
            print("Pedido pago com sucesso")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    
    def cancelar_pedido(self):
        try:
            self.estado_atual.cancelar_pedido()
            print("Pedido cancelado com sucesso")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def despachar_pedido(self):
        try:
            self.estado_atual.despachar_pedido()
            print("Pedido despachado com sucesso")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def set_estado_atual(self, estado: State):
        self.estado_atual = estado


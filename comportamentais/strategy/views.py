from django.shortcuts import render
from .models import PedidoEletronica, PedidoMoveis
from .strategies.frete_expresso import FreteExpresso
from .strategies.frete_comum import FreteComum


# Create your views here.
def index(request):
    # Criando pedidos com estratégias de entrega diferentes
    pedido1 = PedidoEletronica(nome_cliente="Isaac", nome_produto="Celular", valor=100, frete=FreteExpresso())
    pedido2 = PedidoMoveis(nome_cliente="Carlos", nome_produto="Mesa", valor=100, frete=FreteComum())

    context = {
        "pedidos": [
            { "valor": pedido1.valor, "valor_do_frete": pedido1.calcular_frete(), "processamento": pedido1.processar_pedido()},
            { "valor": pedido2.valor, "valor_do_frete": pedido2.calcular_frete(), "processamento": pedido2.processar_pedido()}
        ],
    }

    return render(request, "strategy_index.html", context)
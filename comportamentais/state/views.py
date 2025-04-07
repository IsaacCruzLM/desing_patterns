from django.shortcuts import render
from .models import Pedido


def index(request):
    # Criando pedido
    pedido1 = Pedido()
    pedido2 = Pedido()

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Transiciona pedido 1 (Com sucesso)")
    print(" ")
    pedido1.realizar_pagamento()
    print(" ")
    pedido1.despachar_pedido()
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Transiciona pedido 2 (Com falha)")
    print(" ")
    pedido2.realizar_pagamento()
    print(" ")
    pedido2.despachar_pedido()
    print(" ")
    print("Tentar cancelar pedigo já despachado: ")
    pedido2.cancelar_pedido()
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    context = {}

    return render(request, "state_index.html", context)
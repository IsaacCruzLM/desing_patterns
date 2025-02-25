from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import PagamentoCredito, PagamentoDebito, PagamentoDinheiro


def index(request):
    valor =  1000.0
    pagmento_credito = PagamentoCredito(valor=valor)
    pagmento_debito = PagamentoDebito(valor=valor)
    pagmento_dinheiro = PagamentoDinheiro(valor=valor)

    context = {
        "pagamentos": [
        	f"Crédito: {pagmento_credito.realiza_cobranca()}",
        	f"Débito: {pagmento_debito.realiza_cobranca()}",
        	f"Dinheiro: {pagmento_dinheiro.realiza_cobranca()}",
        ],
    }
    print(context)

    return render(request, "template_method_index.html", context)
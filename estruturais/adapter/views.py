from django.shortcuts import render
from .models import PagFacilAdapter, TopPagamentosAdapter, TopPagamentos, Cobranca


def index(request):
    # Criando adapters
    pag_facil_adapater = PagFacilAdapter()

    top_pagamentos = TopPagamentos()
    top_pagamentos_adapater = TopPagamentosAdapter(top_pagamentos=top_pagamentos)

    cobranca = Cobranca(pag_facil_adapater)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Realiza cobranca com a Classe PagFácil")
    cobranca.set_valor(valor=100)
    cobranca.set_parcelas(parcelas=3)
    cobranca.set_numero_cartao(numero_cartao=123123123)
    cobranca.set_cvv(cvv=111)

    if(cobranca.realizar_pagamento()):
        print("Sucesso")
    else:
        print("Falha")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    cobranca.set_gateway(gateway=top_pagamentos_adapater)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Realiza cobranca com a Classe Top Pagamentos")
    cobranca.set_valor(valor=100)
    cobranca.set_parcelas(parcelas=3)
    cobranca.set_numero_cartao(numero_cartao=123123123)
    cobranca.set_cvv(cvv=111)

    if(cobranca.realizar_pagamento()):
        print("Sucesso")
    else:
        print("Falha")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    context = {}

    return render(request, "adapter_index.html", context)
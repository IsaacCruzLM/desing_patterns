from django.shortcuts import render
from .models import Newsletter, Funcionario, Parceiro, Fornecedor


def index(request):
    # Criando newsletter e modelos
    newsletter = Newsletter()
    funcionario1 = Funcionario(nome="Funcionário 1", email="funcionario1@email.com", subject=newsletter)
    funcionario2 = Funcionario(nome="Funcionário 2", email="funcionario2@email.com", subject=newsletter)
    parceiro1 = Parceiro(nome="Parceiro 1", email="parceiro1@email.com", subject=newsletter)
    fornecedor1 = Fornecedor(nome="Fornecedor 1", email="fornecedor1@email.com", subject=newsletter)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Envia Mensagem 1")
    print(" ")
    newsletter.add_message(message='Primeira Mensagem')
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Remove Funcionario 2 e Envia Mensagem 2")
    print(" ")
    newsletter.remove_observer(funcionario2)
    newsletter.add_message(message='Segunda Mensagem')
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Remove Parceiro e Envia Mensagem 3")
    print(" ")
    newsletter.remove_observer(parceiro1)
    newsletter.add_message(message='Terceira Mensagem')
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Adicona Funcionario 2 novamente e Envia Mensagem 4")
    print(" ")
    newsletter.register_observer(funcionario2)
    newsletter.add_message(message='Quarta Mensagem')
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Reenvia Mensagem 4")
    print(" ")
    newsletter.notify_observers()
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    context = {}

    return render(request, "observer_index.html", context)
from django.shortcuts import render
from .models import Newsletter, Funcionario, Parceiro, Fornecedor


def index(request):
    # Criando newsletter
    newsletter = Newsletter()
    funcionario1 = Funcionario(nome="Funcionário 1", email="funcionario1@email.com", subject=newsletter)
    funcionario2 = Funcionario(nome="Funcionário 2", email="funcionario2@email.com", subject=newsletter)
    parceiro1 = Parceiro(nome="Parceiro 1", email="parceiro1@email.com", subject=newsletter)
    fornecedor1 = Fornecedor(nome="Fornecedor 1", email="fornecedor1@email.com", subject=newsletter)

    newsletter.add_message(message='Primeira Mensagem')

    newsletter.remove_observer(funcionario2)

    newsletter.add_message(message='Segunda Mensagem')

    newsletter.remove_observer(parceiro1)
    
    newsletter.add_message(message='Terceira Mensagem')

    newsletter.register_observer(funcionario2)

    newsletter.add_message(message='Quarta Mensagem')

    newsletter.notify_observers()
    
    context = {}

    return render(request, "observer_index.html", context)
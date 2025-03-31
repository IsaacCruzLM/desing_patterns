from abc import ABC, abstractmethod
from django.db import models


class Observer(ABC):
    class Meta:
        abstract = True  # Django não cria uma tabela para esta classe
    
    @abstractmethod
    def update(self, message: str) -> None:
        pass
    
    @abstractmethod
    def get_nome(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

class Email():
    @staticmethod
    def enviar_email(self, observer: Observer, message: str) -> None:
        print('-----------------------------------------------')
        print('Email enviado para {} - {}'.format(observer.get_nome(), observer.get_email()))
        print('Mesagem: {}'.format(message))
        pass

class Cliente(Observer):
    nome = ""
    email = ""

    def __init__(self, *args, subject: Subject, nome: str, email: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome = nome
        self.email = email
        self.subject = subject

        self.subject.register_observer(self)
    
    def update(self, message: str) -> None:
        Email.enviar_email(self, message)

    def get_nome(self) -> str:
        return self.nome
    
    def get_email(self) -> str:
        return self.email

class Fornecedor(Observer):
    nome = ""
    email = ""

    def __init__(self, *args, subject: Subject, nome: str, email: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome = nome
        self.email = email
        self.subject = subject

        self.subject.register_observer(self)
    
    def update(self, message: str) -> None:
        Email.enviar_email(self, message)

    def get_nome(self) -> str:
        return self.nome
    
    def get_email(self) -> str:
        return self.email

class Funcionario(Observer):
    nome = ""
    email = ""

    def __init__(self, *args, subject: Subject, nome: str, email: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome = nome
        self.email = email
        self.subject = subject

        self.subject.register_observer(self)
    
    def update(self, message: str) -> None:
        Email.enviar_email(self, message)

    def get_nome(self) -> str:
        return self.nome
    
    def get_email(self) -> str:
        return self.email
    
class Parceiro(Observer):
    nome = ""
    email = ""

    def __init__(self, *args, subject: Subject, nome: str, email: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome = nome
        self.email = email
        self.subject = subject

        self.subject.register_observer(self)
    
    def update(self, message: str) -> None:
        Email.enviar_email(self, message)

    def get_nome(self) -> str:
        return self.nome
    
    def get_email(self) -> str:
        return self.email
    
class Newsletter(Subject):
    observers = []
    messages = []

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer) -> None:
        for i in range(len(self.observers) - 1, -1, -1):  # Iterando de trás para frente
            if self.observers[i] == observer:
                self.observers.pop(i) 

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.observers[-1])
    
    def add_message(self, message: str) -> None:
        self.messages.append(message)

        self.notify_observers()
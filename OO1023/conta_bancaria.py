from abc import ABC


class Conta(ABC):
    def __init__(self, nomeCliente) -> None:
        self.nomeCliente = nomeCliente
        self.saldo = None
        self.agencia = None
        self.numConta = None

    def sacar(self): 
        pass


class Pessoa(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.idade = None

    @property
    def idade(self):
        return self.idade
    
    @idade.setter
    def idade(self, idade):
        self.idade = idade
        

class Cliente(Pessoa):
    def __init__(self, nome) -> None:
        super().__init__(nome)

















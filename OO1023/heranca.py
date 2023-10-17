from abc import ABC

# transformando a classe em abstrata
class Pessoa(ABC):
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print(f'{self.nome} é um {self.__class__.__name__}')

class Cliente(Pessoa):
    
    def __init__(self, nome, sobrenome,cartao):
        super().__init__(nome, sobrenome)
        self.cartao = cartao
        

    def falar_nome(self):
        print(f'{self.nome} {self.sobrenome} é um {self.__class__.__name__}')


class Funcionario(Pessoa):
    ...




c1 = Cliente('Mastrogildo', 'Kenny','Visa')

c1.falar_nome()









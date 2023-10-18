import abc



class Pessoa(abc.ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.idade = None

    @property
    def nome(self):
        return self.nome
    
    @property
    def idade(self):
        return self.idade
    
    @idade.setter
    def idade(self, idade):
        self.idade = idade
        

class Cliente(Pessoa):
    def __init__(self, nome) -> None:
        super().__init__(nome)
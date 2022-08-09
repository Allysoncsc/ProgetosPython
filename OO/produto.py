
class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))


    # Getter
    @property
    def preco(self):
        return self._preco


   # Setter
    @preco.setter
    def preco(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$',''))
        self._preco = value

    @property
    def nome(self):
        return self._nome
    
    
    @nome.setter
    def nome(self, value):
        #value = value.replace('a','@')
        self._nome = value.title()
        
        
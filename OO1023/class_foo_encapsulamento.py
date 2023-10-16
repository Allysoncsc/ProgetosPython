
class Food:
    """ class represeting a food """
    def __init__(self, nome, quantidade, preco):
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        self._quantidade = valor

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def nome(self):
        return self._nome
    
    def calcular_venda(self,qtd):
        return self._preco * qtd



pera = Food('Pêra',10,2)

print(f"{pera.nome} esta custando {pera.preco}")
print(f"vc comprou 3 {pera.nome} preco: {pera.calcular_venda(3)}")
















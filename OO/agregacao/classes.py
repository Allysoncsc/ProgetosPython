
from ast import Pass


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
        
    def inserir_produto(self, produto):
        self.produtos.append(produto)
        
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.name, produto.value)
        
        
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.value
        return total
    
    
    
class Produto:
    def __init__(self, name,value):
        self.name = name
        self.value = value
























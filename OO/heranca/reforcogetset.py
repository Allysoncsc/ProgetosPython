class Produto:
    def __init__(self, nome,preco):
        self.nome = nome
        self.preco = preco
        
    
    #Getter
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    #Setter
    @nome.setter
    def nome(self, name):
        self._nome = name.title()
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            #aprender expressoes regulares
            valor = float(valor.replace('R$',''))
            
        self._preco = valor
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))
    
    
    
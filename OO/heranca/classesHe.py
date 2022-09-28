class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
     
     
     
class Aluno(Pessoa):     
    def estudar(self):
        print(f'{self.nome} está estudando')
            
    
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando') 
    
class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome
    
    def comprar(self):
        print(f'{self.nome} {self.sobrenome} é um cliente VIP  e está comprando') 
 
 
 
       
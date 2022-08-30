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
    def comprar(self):
        print(f'{self.nome} é um cliente VIP  e está comprando') 
 
 
 
       
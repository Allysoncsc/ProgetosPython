from abc import ABC, abstractmethod



class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        


    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        if isinstance(value,str):
            raise ValueError("saldo not must be a string")
        
        self._saldo = value
    
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'  Agência: {self._agencia}'
              f'  Conta: {self._conta}'
              f'  Saldo: {self._saldo}')




class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        self.detalhes()
        
        
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
        
    def sacar(self, valor):
       if self._saldo + self._limite < valor:
            print('Saldo insuficiente')
            return 
        
       self._saldo -= valor 
       self.detalhes()
       

class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []
        
        
    def inserir_clientes(self,cliente):
        self.clientes.append(cliente)
        
    def inserir_contas(self,conta):
        self.contas.append(conta)
        
    def autenticar(self,cliente):
        if cliente not in self.clientes:
            return False
        
        if cliente.conta not in self.contas:
            return False
        
        if cliente.conta.agencia not in self.agencias:
            return False
        
        return True
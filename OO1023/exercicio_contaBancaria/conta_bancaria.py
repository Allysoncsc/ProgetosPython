import abc


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo) -> None:
        self.agencia = agencia
        self.saldo = saldo
        self.conta = conta

    @abc.abstractmethod
    def sacar(self,valor): 
        pass

    def depositar(self,valor):
        self.saldo += valor
        self.detalhes(f' Depositou R${valor}')

    def detalhes(self, msg =''):
        print(f'O saldo da conta {self.conta} é: {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        
        if self.saldo - valor >= 0:
            self.saldo -= valor
            self.detalhes(f' Sacou R${valor}')
            return self.saldo
        print('Não foi possível sacar')
        self.detalhes()
        
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0,limite=0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        
        limite_maximo = -self.limite

        if self.saldo - valor >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f' Sacou R${valor}')
            return self.saldo
        print('Não foi possível sacar')
        self.detalhes()
        

if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222,0)
    cp1.sacar(1)
    cp1.depositar(2)
    cp1.sacar(1)

    cc1 = ContaCorrente(111,222,0,100)
    cc1.sacar(1)
    cc1.depositar(2)
    cc1.sacar(1)

















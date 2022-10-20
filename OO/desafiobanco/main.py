from pessoa import Cliente
from conta import ContaPoupanca, ContaCorrente, Banco

print('\n')
banco = Banco()

cliente1 = Cliente('Allyson', 30)


conta1 = ContaCorrente(1111, 1232, 0)

cliente1.inserir_conta(conta1)


if banco.autenticar(cliente1):
    cliente1.conta.sacar(20)
    cliente1.conta.depositar(40)
else:
    print('Cliente não autenticado.')

banco.inserir_clientes(cliente1)
banco.inserir_contas(conta1)


if banco.autenticar(cliente1):
    cliente1.conta.sacar(20)
    cliente1.conta.depositar(40)
else:
    print('Cliente não autenticado.')



print('\n')
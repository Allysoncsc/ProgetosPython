import contas
import class_pessoa
import banco

if __name__ == '__main__':
    c1 = class_pessoa.Cliente('Allyson',33)
    cc1 = contas.ContaCorrente(111,222,0,0)
    c1.conta = cc1

    banco = banco.Banco()
    banco.clientes.extend([c1])
    banco.contas.extend([cc1])
    banco.agencias.extend([111,222,333])

    print(banco.autenticar(c1,cc1))

    c1.conta.depositar(100)









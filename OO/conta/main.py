from contapou import ContaPoupanca
from contacor import ContaCorrente


cp = ContaPoupanca(11,222,0)

print('')
cp.depositar(20)
cp.sacar(15)

print('####################')

cc = ContaCorrente(222,333,200)

cc.depositar(20)
cc.sacar(320)





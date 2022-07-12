
cpf = input('Digite seu CPF:  ')
novo_cpf = cpf[:9]
"""""
c = 10
soma = 0
for n in cpf:
    soma += int(n) * c
    # print('n =',n +' c= ',c,' soma= ',soma)
    c -= 1

digito = 11 - (soma % 11)
print(digito)
if digito > 9:
    digito = 0



print(digito)
"""

reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11

        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)
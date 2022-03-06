"""
and = e
or = ou
not = !
in = se está dentro
not in

aula 27
len = conta quantidade de caracteres, funciona somente com string
aula 29
pass = será implementado depois, o python pula
... = elipse funciona para a mesma coisa
"""



nome = input('Digite seu nome: ')
idade = int(input('Digite idade: '))
qtdCaracteres = len(nome)

if(idade >= 18):
    print(f'{nome}, Você é maior de idade')
    # ficará dentro do if
#e = & = and
elif(idade >=14  and idade < 18):
    print(f'{nome}, vá estudar')
else:
    print(f'{nome}, vá bincar, criança')

if 'son' in nome:
    print(f'Existe son em {nome}')

for n in range(10):
    print(n)
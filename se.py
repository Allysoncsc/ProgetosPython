"""
and = e
or = ou
not = !
in
not in
"""



nome = input('Digite seu nome: ')
idade = int(input('Digite idade: '))

if(idade >= 18):
    print(f'{nome}, Você é maior de idade')
    # ficará dentro do if
#e = & = and
elif(idade >=14  and idade < 18):
    print(f'{nome}, vá estudar')
else:
    print(f'{nome}, vá bincar, criança')


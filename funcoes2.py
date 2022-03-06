# AULA 52 SOBRE FUNÇÕES

def funcaoOla():
    print('Olá mundo ceará')


funcaoOla()

# argumento padrao caso não seja enviado variavel
def dizOi(msg = 'Oi', nome = 'Usuário'):
    nome.replace('e', '3')
    print(msg, nome)

dizOi()
dizOi('Hello','Everybody')
dizOi(nome='Tom')



def mestre(funcao, *args, **kwargs):
    return funcao(*args,**kwargs)

mestre(dizOi,'Hi','guabiru')
mestre(dizOi, 'bom dia', nome='luffy')

#######################################
# AULA 60 - EXPRESSÕES LAMBDAS

def multiplica(arg, arg2):
    return arg * arg2

var= multiplica(2,3)

#expressão que recebe dois valores e multiplica
a = lambda x, y: x*y
print(a(2,3))


lista = [
    ['p1',13]
    ['p2',27]
    ['p3',55]
]
#ordenar por valor indice = 1
def ordena(item):
    return item[1]

lista.sort(key=ordena)
lista.sort(key=ordena, reverse=True)
lista.sort(key=lambda item: item[1])

print(sorted(lista, key=lambda i: i[1]))
#ordenar por nome indice 0
print(sorted(lista, key=lambda i: i[0]))
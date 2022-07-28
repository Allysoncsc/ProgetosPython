from A81map import produtos, pessoas, lista


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2 )
    return p

def aumenta_idade(p):
    p['idade'] = p['idade'] +1
    return p


"""
#função map recebe uma função por isso usei lambda
nova_lista = map(lambda x: x*2, lista)
print(lista)
print(list(nova_lista))

#usando list comprehension
new_lista = [x*2 for x in lista]



for produto in produtos:
    print(produto)
"""
#precos = map(lambda p: p['preco'], produtos)
#for preco in precos:
#   print(preco)
#valor_novo = map(aumenta_preco, produtos)
#for produto in valor_novo:
#    print(produto)

#for name in pessoas:
#    nomes = [x for x in name.items()]
nomes = map(lambda p: p['nome'], pessoas)
#aniversario = map(lambda  p: p['idade'] + 1, pessoas)
print(type(nomes))
for nome in  nomes:
    print(f'{nome}')
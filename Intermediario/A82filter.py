from A81map import produtos, pessoas, lista

#filter
nova_lista = filter(lambda x: x>5,lista)
#list comprehension
#nova_lista = [x for x in lista if x> 5]
print(list(nova_lista))

def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

caros = filter(lambda p: p['preco'] > 30, produtos)

lista_maior = filter(filtra, pessoas)


print(type(caros))
for x in caros:
    print(x)
print()

for m in lista_maior:
    print(m)

'''
count - itertools
'''

from itertools import count

contador =  count(start = 1, step = 0.1)

for valor in contador:
    print(round(valor))

    if valor>=11 or valor <= -10:
        break

nomes = ['Allyson', 'Alailson', 'Alais','Artas']

lista_nomes = zip(contador, nomes)
print(list(lista_nomes))
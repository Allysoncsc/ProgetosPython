from  itertools import count, zip_longest

strin = '0213245642315864756132'
n = 3
#comp = [letra for letra in strin]
#print(comp)

#lista recebe de 3 em 3 caractere da strin
lista = [strin[i:i+n] for i in range(0, len(strin),n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)

# aula 74
#zip para unir iteraveis // existe o zip_longest

indice = count()
cidades = ['São paulo','Belo Horizonte','Salvador','Fortaleza']
estados = ['SP','MG','BA','CE']

cidades_estados = zip(
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(indice,cidade,estado)

lista_a = [10,2,3,5,8,6]
lista_b = [33,55,8,66,74,52,3,5,6,4]

lista_soma = [x+y for x,y in zip(lista_a,lista_b)]

lista_longest = [x+y for x,y in zip_longest(lista_a,lista_b,fillvalue=0)]
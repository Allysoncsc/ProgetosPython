# se cria lista usando o cochete
# para converter algo em lista se usa list()



lista = ['abacaxi','maçã','banana' ]

print(lista)

#append adiciona no final da lista
lista.append('uva')

print(lista)

# pop remove o ultimo item da lista

lista.pop()

#insert adiciona no item escolhido
lista.insert(0,'melão')
#delete remove o indice escolhido


#copy copia para criar outro objeto independente
lista_nova = lista.copy()




iteravel = 0
for fruta in lista:
    print(iteravel, fruta)
    iteravel+=1


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])


#desempacoita só o primeiro valor, o restante vai para outra lista _  (é convenção que indica uma varável que não será usada)
fruta1, *_ = lista

#tuppla se usa parenteses/ tupla é uma lista imutável, não se altera o valor
teste_tupla = ('Alailson','Alaís','Allyson')
convert_tupla = tuple(lista)
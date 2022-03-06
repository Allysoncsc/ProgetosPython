

strin = '0213245642315864756132'
n = 3
#comp = [letra for letra in strin]
#print(comp)

#lista recebe de 3 em 3 caractere da strin
lista = [strin[i:i+n] for i in range(0, len(strin),n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)
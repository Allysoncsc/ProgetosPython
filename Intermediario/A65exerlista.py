

lista_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,6,3,2,8,9,10],
    [1,2,3,4,5,4,2,8,9,10],
    [1,2,3,4,5,5,7,2,6,10],
    [1,2,6,4,7,6,7,2,9,10],
]

def encontra_duplicado(lista):
    """set não aceita duplicado"""
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)

    return primeiro_duplicado

for lista in lista_de_inteiros:
    print(lista, encontra_duplicado(lista))

print(encontra_duplicado([1,2,3,4,5,2]))
print(encontra_duplicado([1,2,3,3,5,2]))
print(encontra_duplicado([1,2,3,1,5,2]))









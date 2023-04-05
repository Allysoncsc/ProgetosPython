
texto = 'python'

i = 0
tamanho_string = len(texto)
iteratador = iter(texto)


while i < tamanho_string:
    print(f'{texto[i]}')
    i += 1



for letra in texto:
    print(f'{letra}')


#Aula 73
while True:
    try:
        letra =next(iteratador)
        print(letra)
    except StopIteration:
        break
#Aula 76 - 
import os

print('Vocêr deve descobrir a palavra')

wordsecret = 'agua'
tentativas = 0
palavra = '****'
letra_acertada = ''


while  tentativas < 6: #wordsecret != palavra:
    os.system('clear')  #limpa o terminal

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Tentativa inválida, digite somente uma letra.')
        continue

    if letra in wordsecret:
        letra_acertada += letra 

    palavra_formada = ''
    for letra_secreta in wordsecret:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    tentativas +=1
    print(f'Tentativa = {tentativas}')
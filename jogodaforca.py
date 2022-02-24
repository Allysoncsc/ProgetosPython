

palavra = 'beliver'
digitadas = []
continuar = 'sim'

while continuar == 'sim':
    letra = input('Digite uma letra: ' )

    if len(letra) > 1:
        print('Ahhh isso não vel, digite apenas uma letra')
        continue

    if letra in palavra:
        print(f'A letra "{letra}" existe na palavra')
        digitadas.append(letra)
    else:
        print(f'A letra {letra} não está na palavra')
        # digitadas.pop() para remover o ultimo

    secretoTemp = ''
    for l in palavra:
        if l in digitadas:
            secretoTemp += l
        else:
            secretoTemp += '*'



    if secretoTemp == palavra:
        print(f'Parabéns, você ganhou, a palavra era {secretoTemp}')
        break
    else:
        print(f'A palavra está assim {secretoTemp}')

    continuar = input('Deseja continuar? ')
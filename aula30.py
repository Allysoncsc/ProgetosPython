numero_inteiro = input('Digite um número ')


if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0 :
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')

# if not numero_inteiro.isdigit():
else:
    print('Não é número')



n1 = input('digite um numero: ')

n2 = input('digite outro numero: ')

operacao = input('digite a operação que você deseja: ')

resultado = 0
continuar = 's'
numero1 = int(n1)
numero2 = int(n2)




if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
elif operacao == '%':
    resultado = numero1 % numero2
else:
    print('você não digitou uma operação válida.')

print(f'{resultado}.')
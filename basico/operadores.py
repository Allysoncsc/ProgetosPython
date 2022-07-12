"""
+
-
*
/
// retoma o resto inteiro da divisão
** exponencial
% resto da divisão
()

"""

nome = 'Allyson Correia'
idade = 31
altura = 1.63
e_maior = idade > 18
peso = 83.2
anoAtual = 2022
anoNascimento = 2002 - idade
n = """40"""
print('Nome: ',nome)
print("Idade: ", idade)
print('Altura: ',altura)
print('É maior: ', e_maior)

imc = peso/(altura * altura)
# altura ** 2

print(nome, ' tem imc = ', imc)
print(type(n))

# da para usar o f string = tamplete string do javascript
print(f'{nome} tem {idade} imc é igual a {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}' .format(nome, idade, imc))

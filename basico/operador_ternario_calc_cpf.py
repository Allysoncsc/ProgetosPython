
import random
import sys

#gerando 9 numero aleatórios
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))


sys.exit()


"""


variavel = 18


print('maior de idade' if variavel >= 18 else 'Menor de idade')




digito = 9
novo_digito = digito if digito <=9 else 0

"""

"""
validar o primeiro digito do CPF:
se pega os 9 primeiros numeros
multiplica regressivamente por 10 a par tir do primeiro 
EX: 7  4 6 8 2 4 8 9 0  - 70
   10  9 8 7 6 5 4 3 2
  soma  o resultado de cada multiplicação 
  multiplica por 10 depois pega o resto da divisão por 11
  se o resultado for menor que 9 usa o resultado
  senão substitui por 0
"""

import re #importando expressões regulares
cpf = input('Digite seu CPF:  ')
cpf_sem_ponto = re.sub(
    r'[^0-9]', #substitui tudo que não for numero
    '',        #substitui por espaço em branco
    cpf        #valor
)




#74682489070
cpf = input('Digite seu CPF:  ').replace('.','').replace('-','')
novo_cpf = cpf[:9] #pega do indice 0 até  8
contador_regressivo = 10 #usado para mutiplicar

resultado =0
for digito in novo_cpf:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

p_digito = resultado * 10 % 11
p_digito = p_digito if p_digito <= 9 else 0

print(p_digito)



"""
validar o segundo digito do CPF:
se pega os 9 primeiros numeros e adiciona o primeiro digito
multiplica regressivamente por 11 a par tir do primeiro 
EX: 7  4  6 8 2 4 8 9 0 7 - 70
    11 10 9 8 7 6 5 4 3 2
  soma  o resultado de cada multiplicação 
  multiplica por 10 depois pega o resto da divisão por 11
  se o resultado for menor que 9 usa o resultado
  senão substitui por 0
"""

novo_cpf += str(p_digito)
resultado =0
contador_regressivo = 11
for digito in novo_cpf:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

s_digito = resultado * 10 % 11
s_digito = s_digito if s_digito <= 9 else 0

print(s_digito)
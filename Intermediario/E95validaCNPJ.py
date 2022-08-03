import re
import random

def chama_funcoes(cnpj):
    cnpj = remover_caracteres(cnpj)
    print(f' removeu caracteres = {cnpj} ')
    cnpj = remove_dois_digitos(cnpj)
    print(f' removeu os dois ultimos digitos = {cnpj} ')
    cnpj = digito_um(cnpj)
    cnpj = digito_um(cnpj)
    return cnpj


def remover_caracteres(cnpj):
    #subtitui tudo que não for de 0 a 9 por nada
    return re.sub(r'[^0-9]', '',cnpj )



def remove_dois_digitos(cnpj):
    size = len(cnpj)
    final_str = cnpj[:size - 2]
    return final_str


def adiciona_digito(cnpj, valor):
    if valor > 9:
        valor = 0

    digito =  str(valor)
    cnpj += digito
    return cnpj


def digito_um(cnpj):

    if len(cnpj) == 12:
        m = 5
    else:
        m = 6

    total = 0

    for i in cnpj:
        numero = int(i)
        if m == 1:
            m = 9

        total += m * numero
        #print(f'{m} * {numero} = {m * numero}')
        m -= 1

    valor = (11 - (total % 11))
    cnpj = adiciona_digito(cnpj,valor)
    return cnpj

def gera():
    dois_digitos = random.randint(10,99)
    segundo_bloco = random.randint(100,999)
    terceiro_bloco = random.randint(100,999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{dois_digitos}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'
    return inicio_cnpj

def formata(cnpj):
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
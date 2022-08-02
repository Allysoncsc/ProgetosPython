import re


def chama_funcoes(cnpj):
    cnpj = remover_caracteres(cnpj)
    print(f' removeu caracteres = {cnpj} ')
    cnpj = remove_dois_digitos(cnpj)
    print(f' removeu os dois ultimos digitos = {cnpj} ')
    cnpj = digito_um(cnpj)
    cnpj = digito_dois(cnpj)
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
    size = len(cnpj)
    m = 5
    total = 0

    for i in cnpj:
        numero = int(i)
        if m == 1:
            m = 9

        total += m * numero
        #print(f'{m} * {numero} = {m * numero}')
        m -= 1

    valor = (11 - (total % 11))
    #print(valor)
    cnpj = adiciona_digito(cnpj,valor)
    return cnpj


def digito_dois(cnpj):
    size = len(cnpj)
    m = 6
    total = 0

    for i in cnpj:
        numero = int(i)
        if m == 1:
            m = 9

        total += m * numero
        # print(f'{m} * {numero} = {m * numero}')
        m -= 1

    valor = (11 - (total % 11))
    #print(valor)
    cnpj = adiciona_digito(cnpj, valor)
    return cnpj

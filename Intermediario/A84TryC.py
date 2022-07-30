

a = 0

try:
    print(a)
except NameError as erro:
    print('Erro', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Será executado se não achar nenhum erro')
finally:
    print('será executado independente do erro')


def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print(error)
        return False


def div(n1,n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return  n1/n2

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

#numero = float(input('Digite um número: '))  || numero = converte_numero(numero)
numero = converte_numero(input('Digite um número: '))

if numero is not None:
    print(numero * 5)
else:
    print('Não é número')





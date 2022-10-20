from contextlib import contextmanager


@contextmanager
def abrir (arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('abc.txt','w') as arquivo:
    arquivo.write('Linha \n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha 3 \n')





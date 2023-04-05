def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)





#se não passar agurmento ele preenche como sem nome
def imprimir(nome = 'Sem nome'):
    print(f'Olá {nome}')
    


def soma(x,y,z =None):
    if z is not None:
        print(f'{x}= {y=} {z=} , x+y+z')
    else:
        print(f'{x=} {y=}',x+y )

soma(1,2)
soma(7,9,0)










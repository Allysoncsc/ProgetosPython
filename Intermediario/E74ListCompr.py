

carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3',50))


total = sum([float(y) for x,y in carrinho])
print(total)




def lista_de_clientes(clientes_iteravel, lista = None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


def dobraLista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    m = 1
    for i in lista:
        m *= i
    return m
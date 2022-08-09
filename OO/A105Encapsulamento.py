"""
public, protected, private
_ protected
__ private
"""




class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados
        
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd  = BaseDeDados()

bd.inserir_cliente(1,'Allyson')
bd.inserir_cliente(2,'Keliane')
bd.inserir_cliente(3,'Diamond')

bd.lista_clientes()
print()
print(bd.dados)

print()
bd.apagar_cliente(3)
print()
bd.lista_clientes()


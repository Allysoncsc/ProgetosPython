

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.dados['clientes'][id]


bd  = BaseDeDados()

bd.inserir_cliente(1,'Allyson')
bd.inserir_cliente(2,'Keliane')
bd.inserir_cliente(3,'Diamond')

bd.lista_clientes()

bd.apagar_cliente(3)
print()
bd.lista_clientes()


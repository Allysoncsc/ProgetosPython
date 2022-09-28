class BaseDeDados:
    def __init__(self):
        self.dados = {}
    
    def inserir_cliente(self,id,nome):
        if 'cliente' not in self.dados:
            self.dados['cliente'] = {id:nome}
        else:
            self.dados['cliente'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)
            
    def apagar_cliente(self,id):
        del self.dados['cliente'][id]
    
    
    
    
    
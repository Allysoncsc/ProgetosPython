from clahemult import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self,nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._name} não está ligado'
            print(info)
            self.log_warn(info)
            return
        
        if self._conectado:
            info = f'{self._name} já está conectado'
            self.log_warn(info)
            return 
        
        info = f'{self._name} CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True
    
    def desconectar(self):
        if not self._conectado:
            info = f'{self._name} já está desconectado'
            print(info)
            self.log_warn(info)
            return 
        
        info = f'{self._name} DESCONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = False
    









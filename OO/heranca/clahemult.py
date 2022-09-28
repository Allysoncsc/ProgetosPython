class Eletronico:
    def __init__(self, name):
        self._name = name
        self._ligado = False
        
        
    def ligar(self):        
        if self._ligado:
            return
        
        print(f'{self._name} LIGADO')
        self._ligado = True
        
    def desligar(self):
        if not self._ligado:
            return
        
        print(f'{self._name} desligando')
        self._ligado = False
        
        
        

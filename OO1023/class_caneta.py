
class Caneta:
    """
    classe representing a pen
    """

    def __init__(self,cor):
        self._cor = cor
        self._tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):     
        self._cor = valor


    @property
    def tampa(self):
        return self._tampa
    
    @tampa.setter
    def tampa(self, valor):
        self._tampa = valor


caneta1 = Caneta('Azul')
caneta1.tampa = 'Preta'

print(caneta1._cor)
print(caneta1._tampa)






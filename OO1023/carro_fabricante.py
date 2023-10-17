

class Motor:
    def __init__(self,nome,potencia):
        self.nome = nome
        self.potencia = potencia

class Carro:
    def __init__(self,nome, fabricante):
        self.nome = nome
        self.fabricante = fabricante
        self.motor = None

                


class Fabricante:
    def __init__(self,nome):
        self._nome = nome
        self._carros = []

    @property
    def nome(self):
        return self._nome

    def inserir_carros(self, *carros):
        for carro in carros:
            self._carros.append(carro)

    def listar_carros(self):
        for carro in self._carros:
            print(carro.nome, carro.motor)


motorv8 = Motor('V8',80)
motorv30 = Motor('V30',300)


toyota = Fabricante('Toyota')
chevrolet = Fabricante('Chevrolet')
wolkswagen = Fabricante('Wolksgaen')














# class MyRepr:
#     def __repr__(self) -> str:
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

"""
usando decorador para as classes terem função adiciona repr
"""
def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

@adiciona_repr
class Motor:
    def __init__(self,nome,potencia):
        self.nome = nome
        self.potencia = potencia

@adiciona_repr
class Carro:
    def __init__(self,nome, fabricante):
        self.nome = nome
        self.fabricante = fabricante
        self.motor = None

                

@adiciona_repr
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












import enum

# Direcoes = enum.Enum('Direcoes',['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2


def mover(direcao):
    if not isinstance(direcao,Direcoes):
        raise ValueError('Diereção não encontrada')

    print(f'Movendo para a direção {direcao}')

mover(Direcoes.DIREITA)
import random

jog1 = 'ilana'
vida1 = 10
jo2 = 'allyson'
vida2 = 10
dano = 0


def ataque(atacante, defensor):
    print(f'o {atacante} está atacando')

    dado1 = random.randint(0,12)
    print(f'dado do atacante = {dado1}')

    dado2 = random.randint(0,12)
    print(f'dado do defensor = {dado2}')

    if(dado1 > dado2):
        print('o ataque venceu')
        dano = dado1 - dado2

        if defensor == jo2:
            vida2 -= dano   
        elif defensor == jog1:
            vida1 -= dano
        print(f'vida do jogador = {vida2}')
    else:
        print('o jogador defendeu o ataque :D')



while vida1 > 0 or vida2 > 0:
    ataque(jog1,jo2)
    ataque(jo2,jog1)













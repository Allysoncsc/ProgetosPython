# aula 63

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '4'
        },
        'resposta_certa': 'c'
    },

    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '5',
            'b': '6',
            'c': '7'
        },
        'resposta_certa': 'b'
    },

    'Pergunta 3': {
        'pergunta': 'Quanto é 5*5? ',
        'respostas': {
            'a': '20',
            'b': '25',
            'c': '30'
        },
        'resposta_certa': 'b'
    },

    'Pergunta 4': {
        'pergunta': 'Quanto é 8/4? ',
        'respostas': {
            'a': '4',
            'b': '2',
            'c': '3'
        },
        'resposta_certa': 'b'
    },

    'Pergunta 5': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '5',
            'b': '6',
            'c': '7'
        },
        'resposta_certa': 'b'
    },
}

repostas_certas = 0
print()
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns !!!!!! você acertou')
        repostas_certas += 1
    else:
        print('Você errou!')

    print()

qt_per = len(perguntas)
porcentagem = repostas_certas / qt_per * 100
print(f'você acertou {repostas_certas}')
print(f'Porcentagem de acerto: {porcentagem}%')

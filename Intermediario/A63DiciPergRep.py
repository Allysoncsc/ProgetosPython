


perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Quanto é 2+2',
        'opcoes' : {
            'a': '2',
            'b': '4',
            'c': '6',
            'd': '8',
        },
        'gabarito' : 'b'
    },
    'Pergunta 2': {
            'pergunta' : 'Quanto é 8*3',
            'opcoes' : {
                'a': '24',
                'b': '42',
                'c': '16',
                'd': '18',
            },
            'gabarito' : 'a'
        },
    'Pergunta 3': {
        'pergunta': 'Quanto é 5*6',
        'opcoes': {
            'a': '20',
            'b': '40',
            'c': '30',
            'd': '35',
        },
        'gabarito': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 18-9',
        'opcoes': {
            'a': '11',
            'b': '10',
            'c': '8',
            'd': '9',
        },
        'gabarito': 'd'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 4*3',
        'opcoes': {
            'a': '12',
            'b': '14',
            'c': '16',
            'd': '10',
        },
        'gabarito': 'a'
    },
    'Pergunta 6': {
        'pergunta': 'Quanto é 7+15',
        'opcoes': {
            'a': '21',
            'b': '22',
            'c': '23',
            'd': '24',
        },
        'gabarito': 'b'
    },

}

respostas_certas = 0
for chave_p, pergunta_values in perguntas.items():
    print(f'{chave_p} : {pergunta_values["pergunta"]}')

    print('Opções')
    for rk, rv in pergunta_values['opcoes'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pergunta_values['gabarito']:
        respostas_certas +=1
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas')
print(f' {porcentagem_acerto}% das questões')



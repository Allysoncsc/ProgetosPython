"""formato mais usado para criar dicionario"""
d1 = {'chave1':'Valor da chave 1'}
"""adicionando chave e valor"""
d1['chave2'] = 'valor da chave 2'

print(d1)
print(d1['chave1'])

"""outra opção de criação de chave"""
d2 = dict(chave1 = 'Valor chave 1', chave2= 'Valor da chave 2')


if d1.get('chave1') is not None:
    print(d1.get('chave1'))

""" Mudando o valor da chave min 11:39 a62"""
d1['chave1'] = 'Mudei o valor da chave'

"""Deletando chave"""
del d2['chave2']

""" função len mostra quantos pares tem dentro do dicionario"""
print(len(d1))

d3 = {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3',
}

"""Formas de iteração a62 min18:36"""
for v in d3.values():
    print(v)

for k in d3.items():
    print(k[0], k[1])

for k, v in d3.items():
    print(k, v)


clientes = {
    'cliente1' : {
        'nome' : 'Allyson',
        'sobrenome' : 'Correia'
    },

    'cliente2' : {
        'nome' : 'Maria',
        'sobrenome' : 'Keliane'
    }
}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        """\+t é para da tab na linha"""
        print(f'\t{dados_k} = {dados_v}')


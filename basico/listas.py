




l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
print(l1)
print(l2)
#adiciona o l2
l1.extend(l2)
#adiciona
l2.append('b')
#adiciona no indece 0
l2.insert(0, 'Maçã')

print(l1)
print(l2)



lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
    ]

d1 = {x:y.upper() for x,y in lista}
print(d1)

""" dicionario de 1 até 5, o valor é x elevado a 2"""
d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2, type(d2))
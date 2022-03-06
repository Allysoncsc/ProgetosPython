lista = [
    ('chave',2),
    ('chave2', 'valor2')
]
print(type(lista))
d1 = {x.upper() :y*2 for x , y in lista}
print(lista)
print(d1, type(d1))

d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2, type(d2))
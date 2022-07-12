
carrinho = []

carrinho.append(('Camisa1',25))
carrinho.append(('Camisa2',55))
carrinho.append(('Camisa3',20))


total = []
for valor in carrinho:
    total.append(valor[1])

print(sum(total))

totalc = [v[1] for v in carrinho]
print(sum(totalc))

totalr = sum([float(y) for x, y in carrinho])
print(totalr)

from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()



p1 = Produto('Caneta',200)
p2 = Produto('mipad5',1450)
p3 = Produto('teclado',160)



carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)


carrinho.lista_produto()

print(f'total = {carrinho.soma_total()}')


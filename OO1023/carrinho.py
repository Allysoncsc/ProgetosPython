
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir_produto(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        self._produtos.extend(produtos)
        # self._produtos += produtos


class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

p1,p2 = Produto('Caneta',1.20), Produto('Caderno', 20)

carrinho = Carrinho()
carrinho.inserir_produto(p1,p2)

carrinho.listar_produtos()














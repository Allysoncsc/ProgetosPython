"""
Funções - def
"""


def funcao():
    print('Hello World')
"se não passar os argumentos, serão usados os argumentos padrões"
def saudacao(msg = 'Olá',nome='Usuário'):
    nome = nome.replace('e','3')
    print(msg, nome)

saudacao()
saudacao('Hello','Allyson')
saudacao(nome='Mr')











# associao, os objetos sao independentes

from classes import Escritor
from classes import Caneta

escritor = Escritor('Allyson')
print(escritor.nome)


caneta = Caneta('Bic')

#envia todo o objeto para escritor.ferramenta
escritor.ferramenta = caneta

escritor.ferramenta.escrever()


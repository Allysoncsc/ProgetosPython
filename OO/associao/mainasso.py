from classes import Escritor
from classes import Caneta

escritor = Escritor('Allyson')
print(escritor.nome)


caneta = Caneta('Bic')

escritor.ferramenta = caneta

escritor.ferramenta.escrever()


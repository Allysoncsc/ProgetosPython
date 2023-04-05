
#Aula 90 - 
import os

#print('Vocêr deve descobrir a palavra')

opcao =''

while  opcao != 's':
    os.system('clear')  #limpa o terminal

    opcao = input('[i]nserir [a]pagar [l]istar [s]air')

    lista = []

    if opcao == 'i':
        elemento = input('Digite o elemento a ser inserido: ')
        lista.append(elemento)

    elif opcao == 'l':

        if len(lista) == 0:
            print('Não há nada na lista')
            continue
        
        #for indice in len(lista):
            #print(indice,lista[indice])
        for i, valor in enumerate(lista):
            print(i,valor)

    elif opcao == 'a':
        indice_input = input('Digite o indice a ser apagado: ')

        try:    
            indice = int(indice_input)

            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
            
    else:
        print('Por favor digite umas das opções: i,a,l,s')












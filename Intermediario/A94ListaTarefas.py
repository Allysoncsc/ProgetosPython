

listaTarefas = []
redo_lista = []
continuar =  True


def escolha():
    while(opcao != '5' or opcao != '4' or opcao != '3' or opcao != '2' or opcao != '1'):
        print('')
        print('1. Adicionar tarefa')
        print('2. Listar tarefa')
        print('3. Desfazer tarefa')
        print('4. Refazer tarefa')
        print('5. Sair da função')
        opcao = input('Sua opção ')
        if(opcao != '5' or opcao != '4' or opcao != '3' or opcao != '2' or opcao != '1'):
            print('Opção inválida, escolha novamente')

    return opcao

def do_undo(todo_list, redo_lista):
    if not todo_list:
        print('Lista vazia')
        return
    last_todo = todo_list.pop()
    redo_lista.append(last_todo)


def do_redo(todo_list, redo_lista):
    if not redo_lista:
        print('Nada a refazer')
        return

    last_redo = redo_lista.pop()
    todo_list.append(last_redo)



def programa(lista, redo_lista, continuar):
    while(continuar == True):

        opcao = escolha()


        if opcao == '5':
            continuar = False

        if opcao == '1':
           ntarefa =  input('Adicione tarefa: ')
           lista.append(ntarefa)

        if opcao == '2':
            for tarefa in lista:
                print(tarefa)

        if opcao == '3':
            do_undo(lista,redo_lista)

        if opcao == '4':
            do_redo(lista, redo_lista)





programa(listaTarefas, redo_lista, continuar)



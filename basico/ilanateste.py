

'''
print('\n')
print('\n')
filme = 'vingadores'
ani = input(f'digite o nome de um anime, {filme} não é um anime: ')


print('\n')
print('\n')
print(f'hello world')
print('\n')
print('\n')

print(f'anime digitado {ani}')


senha = input('digite sua senha: ')

if(senha == 'senha'):
    print('Vc está logado')
else:
    print('senha errada')

'''
print('\n')

print('formulário para vingadores')
print('\n')
usuario = input('cadastr seu id: ')
senha = input('cadastre sua senha')


print('\n')

i = 1

print('você está tentando logar')
while i < 5:
    usuario2 = input('digite seu i: ')
    senha2 = input('digite sua senha: ')



    if(usuario2 != usuario):
        print('você errou o usuário')
    if(senha != senha2):
        print('você errou a senha')
    else:
        print('você está logado')
        break

    print(f'essa foi sua tentativa {i}')
    i += 1 








from itertools import groupby, tee


alunos = [
    {'nome' : 'Luiz' , 'nota' : 'A'},
    {'nome' : 'Marcelo' , 'nota' : 'B'},
    {'nome' : 'Otavio' , 'nota' : 'C'},
    {'nome' : 'Pedro' , 'nota' : 'D'},
    {'nome' : 'Guabi' , 'nota' : 'A'},
    {'nome' : 'Adamastor' , 'nota' : 'B'},
    {'nome' : 'Antonio' , 'nota' : 'C'},
    {'nome' : 'Mirosvaldo' , 'nota' : 'D'},
    {'nome' : 'Jumeninalda' , 'nota' : 'B'},
    {'nome' : 'Afonso' , 'nota' : 'A'},

]

#for aluno in alunos:
#    print(aluno)
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados  = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    #é preciso fazer duas cópias pois o for esgota o iterador
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    quantidade =  len(list(va1))
    print(f'\t{quantidade} alunos tiraram  nota {agrupamento}')
    for aluno in va2:
        print(f'\t{aluno}')











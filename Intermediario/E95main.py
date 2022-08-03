import E95validaCNPJ as cnpj


variavel = cnpj.chama_funcoes('04.252.011/0001-10')
print(variavel)


testegera = cnpj.gera()
print(testegera)

testegera = cnpj.chama_funcoes(testegera)
print(testegera)
testegera = cnpj.formata(testegera)
print(testegera)
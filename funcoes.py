"""""
contador = 0
regredir = 10
while contador <=8:
    print(contador, regredir)
    regredir -=1
    contador +=1

print('#######################')

for p,r in enumerate(range(10,1,-1)):
    print(p , r)
"""

def divide(n1,n2):
    return n1/n2

#print('divisao de 8/2 é: ',divide(8,2))
def soma(n1=0,n2=0,n3=0):
    return n1+n2+n3

def perc(n1,per):
    n1 += n1 * (per/100)
    print(n1)
#perc(100 , 10)

def sayHei(saudacao, nome):
    print(saudacao, nome)

#sayHei('Hei', 'Allyson')

def fizzBuzz(n):
    if(n % 5 == 0 and n % 3 == 0):
        return 'FizzBuzz'
    elif(n% 5 == 0):
        return 'Fizz'
    elif(n%3 == 0):
        return 'Buzz'
    else:
        return n

resposta = fizzBuzz(15)
print(resposta)
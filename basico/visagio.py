

x = 0
i = 1
""" print(f'{x} e {i}') 

x = x**i
print(f'{x} e {i}') 

x= x^i
print(f'{x} e {i}') 
while x < 1032:
    x = 2**x 
    
    print(f'{x=} e {i=}') 
    i = i + 1 
 """

teste = (4,6,3,16,9)

lambda x: (x^2) - 3 if x<9 else x + 5

soma =0
for num in teste: 
    soma += (num^2) - 3 if num<9 else num + 5


print(soma)
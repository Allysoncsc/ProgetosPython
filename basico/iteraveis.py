import sys
import time

def gera():
    r = []
    for n in range(20):
        r.append(n)
        time.sleep(0.2)
    return r

g = gera()

for v in g:
    print(v)

#gerador é só colocar entre parenteses
#ocupa menos lugar na memória
#l1 é lista normal e l2 é gerador
l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))
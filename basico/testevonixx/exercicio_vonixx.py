for i in range(10):
    if i % 3 == 0:
        print(i)


for n in range(10):
    fatorial = 1

    if n > 1:
        num = n
        while num > 0:
            fatorial *= num
            num -= 1
    print(f"o fatorial de {n} é {n-1} * {n} = {fatorial}")

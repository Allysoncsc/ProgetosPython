




l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
print(l1)
print(l2)
#adiciona o l2
l1.extend(l2)
#adiciona
l2.append('b')
#adiciona no indece 0
l2.insert(0, 'Maçã')

print(l1)
print(l2)
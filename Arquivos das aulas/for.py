"""lista=[1,2,3,4,5,6,7,8,9,10]

for indice in lista:#Itera cada indice da lista, fazendo uma cópia para a variável indice
    print(indice)
"""
"""lista=[1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    print(i)"""
lista=[1,2,3,4,5,6,7,8,9,10]
lista = [x * x for x in lista]
print(lista)
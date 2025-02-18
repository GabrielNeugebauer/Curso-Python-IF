"""cont=0
while True:
	cont+=1
	input(f"Esse código irá executar infinitamente. Já executou {cont} vezes")"""
"""lista = [1, 2, 3, 4, 5]
valor = 3
while valor in lista:
    print(valor)  # Imprime 1, depois remove
    lista.remove(valor)
print(lista)"""
lista = [1, 2, 3, 4, 5]
valor = 3
cont=0
while cont<len(lista):
    if lista[cont]==valor:
        print(valor)  # Imprime 3, depois remove
        lista.pop(cont)
    cont+=1
print(lista)
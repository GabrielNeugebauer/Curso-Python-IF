Outro tipo de laço de repetição é o while. Com ele, podemos repetir um trecho de código enquanto uma condição for verdadeira.
Exemplo:
```python
cont=0
while True:
	cont+=1
	input(f"Esse código irá executar infinitamente. Já executou {cont} vezes")
```
Exemplo 2:
```python
lista = []
x = 1
while x <= 10:
    lista.append(x * x)#Calcula o quadrado dos números de 1 a 10
    x += 1
print(lista)
```
O While in não funciona da mesma forma que o for. Enquanto o for itera cada um dos elementos de uma lista, o while in verifica se uma condição é verdadeira. É similar ao "\=\=".Exemplo 3:
```python
lista = [1, 2, 3, 4, 5]
valor = 3

while valor in lista:
    print(valor)  # Imprime 3, depois o remove da lista
    lista.remove(valor)
print(lista)
```
Um código com a mesma função do exemplo 3 é:
```python
lista = [1, 2, 3, 4, 5]
valor = 3
cont=0
while cont<len(lista):
    if lista[cont]==valor:
        print(valor)  # Imprime 3, depois remove
        lista.pop(cont)
    cont+=1
print(lista)
```
As vezes, precisamos repetir um determinado trecho de código várias vezes até que uma situação seja suprida. Uma das formas de fazer essa repetição é com o for:
```python
lista=[1,2,3,4,5,6,7,8,9,10]
for indice in lista:#Itera cada indice da lista, fazendo uma cópia para a variável indice
	print(indice)
```
Também é possível utilizar um contador para controlar a quantidade de iterações:
```python
for i in range(10):
	print(i)
```
Conteúdo extra:
Também é possível utilizar o for em formato de list comprehension, como por exemplo:
```python
lista=[1,2,3,4,5,6,7,8,9,10]
lista = [x * x for x in lista]
print(lista)
```
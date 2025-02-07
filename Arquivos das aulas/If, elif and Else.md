O comando if testa se uma condição é ou não verdadeira, assim possibilitando uma tomada de decisão a partir de dados já existentes no momento. Este comando é útil em casos onde há duas ou mais possibilidades de situações as quais o código precisará lidar.
```python
nota = float(input("Digite a nota final do aluno: "))
if nota >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado")
```
Há casos onde são necessárias mais de 2 opções. Nesse caso, basta encadearmos um if dentro do outro:
Exemplo: Organize 3 números em ordem crescente:
```python
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if (n1<n2 and n1<n3):
    if (n2<n3):
        print(f"A sequência em ordem crescente é: {n1}, {n2}, {n3}")
    else:
        print(f"A sequência em ordem crescente é: {n1}, {n3}, {n2}")
else:                          
    if (n2<n1 and n2<n3):
        if (n1<n3):
            print(f"A sequência em ordem crescente é: {n2}, {n1}, {n3}")
        else:
            print(f"A sequência em ordem crescente é: {n2}, {n3}, {n1}")
    else:
        if (n2<n1):
            print(f"A sequência em ordem crescente é: {n3}, {n2}, {n1}")
        else:
            print(f"A sequência em ordem crescente é: {n3}, {n1}, {n2}")
```

O código está funcional, porém há formas mais legíveis de escreve-lo, uma delas é utilizando o comando ***elif***, que mescla um else e um if encadeado, no mesmo comando. Utilizando elif, o código fica desta forma:

 ```python
 n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if (n1<n2 and n1<n3):
    if (n2<n3):
        print(f"A sequência em ordem crescente é: {n1}, {n2}, {n3}")
    else:
        print(f"A sequência em ordem crescente é: {n1}, {n3}, {n2}")
elif (n2<n1 and n2<n3):
    if (n1<n3):
        print(f"A sequência em ordem crescente é: {n2}, {n1}, {n3}")
    else:
        print(f"A sequência em ordem crescente é: {n2}, {n3}, {n1}")
elif (n2<n1):
    print(f"A sequência em ordem crescente é: {n3}, {n2}, {n1}")
else:
        print(f"A sequência em ordem crescente é: {n3}, {n1}, {n2}")
```
Note que a quantidade de linhas diminuiu significativamente, e o código mantém a mesma função.
            
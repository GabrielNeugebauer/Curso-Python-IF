Para interagirmos com alguma informação digitando pela linha de comando, é necessário o uso do comando input. Este comando permite imprimir algo na tela e receber alguma entrada do teclado, a qual pode ser armazenada e utilizada caso necessário. 
Exemplo:
```python
nome = input("Digite o seu nome: ") #Saída: Digite o seu nome: (e aguarda o usuário digitar)
print(f"Seu nome é {nome})
```
Então vamos fazer uma calculadora simples para testar:
```python
n1 = input("Digite o primeiro numero: ") #Saída: Digite o primeiro numero: (e aguarda o usuario digitar)
n2 = input("Digite o segundo numero: ") #Saída: Digite o segundo numero: (e aguarda o usuario digitar)
print(f"O resultado é: {n1+n2}") #Ex. n1=1,n2=1 Saída: O resultado é 11
```
Mas porque isso acontece? 
Em python, toda entrada de dados é por padrão tratada como string. inclusive podemos checar o tipo de dado que está armazenado com o comando type():
```python
print(type(n1)) #Saída: <class 'str'>
```
Para especificar como um dado deve ser tratado no input, é necessário converter o dado na entrada. Corrigindo a calculadora, fica:
```python
n1 = float(input("Digite o primeiro numero: ")) #Saída: Digite o primeiro numero: (e aguarda o usuario digitar)
n2 = float(input("Digite o segundo numero: ")) #Saída: Digite o segundo numero: (e aguarda o usuario digitar)
print(f"O resultado é: {n1+n2}") #Ex. n1=1,n2=1 Saída: O resultado é 2.0
```
No python, existem vários tipos de variáveis, sendo os principais:

Int: números inteiros, sem valores após a vírgula
float: números com ponto flutuante (Valores após a vírgula)
str: String, conteúdo de texto, uma lista de caracteres
bool: Valor Booleano, pode guardar uma informação de true ou false
list: lista capaz de guardar vários elementos, identificados por um índice.
Tupla: lista com valores imutáveis. após criar uma tupla, o valor de cada uma das posições dela será sempre constante.
dict: estrutura de dados que armazena pares **chave: valor**

Para identificar qual o atual tipo de dados mantidos na variável, podemos utilizar o comando type()

```python
inteiro=1
floatnumber=1.00
string="teste"
boolean=False
lista=[]
tupla=()
dicionario={}

print(type(inteiro))#<class 'int'>
print(type(floatnumber))#<class 'float'>
print(type(string))#<class 'str'>
print(type(boolean))#<class 'bool'>
print(type(lista))#<class 'list'>
print(type(tupla))#<class 'tuple'>
print(type(dicionario))#<class 'dict'>
```
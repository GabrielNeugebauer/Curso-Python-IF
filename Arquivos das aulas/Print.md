Para que o programa possa interagir com o usuário pelo terminal, é necessário que haja a escrita e entrada de dados, que podem ser feitas pelos comandos:

***print()***: Escreve alguma informação na saída corrente. Essa informação pode ser de qualquer tipo primitivo, podendo ser string, int, float e boolean. Além disso, ao imprimirmos Strings, podemos utilizar tanto o sinal de ', quanto o sinal de ", pois ambos tem a mesma função.
Exemplos:
```python
print("Meu nome é Pedro")
print(10)
print(False)
print(0.001)
```
Também podemos mesclar tipos diferentes de dados na saída do print. Existem varias formas de fazer isso, porém nesse curso vamos utilizar o formato de f strings, que nos permite chamar variáveis, funções e argumentos lógicos (tipo o if e else) dentro de um print:
```python
idade = 17 #Valor int
nota = 6.0 #Valor float
print(f"Meu nome é Pedro e tenho {idade} anos.") #Saída: Meu nome é Pedro e tenho 17 anos
print(f'João tem nota {nota} e irá {"passar" if nota>=6 else "rodar"} esse ano') # Saída: João tem nota 6.0 e irá passar esse ano
```
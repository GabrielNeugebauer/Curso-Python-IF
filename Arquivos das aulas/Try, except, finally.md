Já pensou no caso de você criar uma variável que espera um valor inteiro, e o usuário insere um valor em string que não pode ser convertido para inteiro? isso daria um erro e quebraria a execução do programa, porém para resolver esse problema, podemos realizar o tratamento de exceções com o comando try, como no exemplo:
```python
while True:
    try:
        #código para tentar executar. Se acontecer algum erro, o respectivo except será acionado.
        numeroa = int(input("Digite um número: "))
        numerob = int(input("Digite outro número: "))
        print(numeroa / numerob)
        break  # Sai do loop se não houver erro
    except ZeroDivisionError:
        #Código para se executar caso ocorra especificamente o erro de divisão por zero.
        print("Ocorreu uma divisão por zero, reiniciando o programa.")
    except Exception as error:
        #Nesse contexto, a palavra chave "as" permite que guardemos uma cópia do erro em uma variável, algo proxímo do que chamamos de um alias, para poder utilizá-lo posteriormente.
        #Exceção genérica, se refere a qualquer exceção não citada acima
        print(f"Ocorreu o erro {type(error)}, reiniciando o programa.")
    finally:
        print("Esta interação com o try foi completa.")  # Sempre será executado
```
Dessa forma, esse código irá realizar a divisão de um numero pelo outro, garantindo que não haverá erros. 
OBS: o programador é livre para escrever quantos excepts preferir, desde que não repita a mesma exceção. O uso do finally não é obrigatório.
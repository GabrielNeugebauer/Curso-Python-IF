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

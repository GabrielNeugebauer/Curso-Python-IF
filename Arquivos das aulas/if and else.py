#Regras: Nessa locadora de jogos, se jogar menos de uma hora, paga 3 reais a hora. Se jogar entre 1 e 2 horas, paga 2,90, e se jogar mais de duas horas, paga 2,80 
hora1, minuto1 = input("Digite a hora em que começou a jogar: ").split(":")
hora2, minuto2 = input("Digite a hora em que terminou de jogar: ").split(":")
hora1, minuto1 = int(hora1), int(minuto1)
hora2, minuto2 = int(hora2), int(minuto2)

if hora1<hora2:
    total_horas = hora2-hora1
else:
    total_horas = 24-hora1+hora2
if minuto1<minuto2:
    total_minutos = minuto2-minuto1
else:
    total_horas = 60-minuto1+minuto2
if total_horas==0:
    print(f"Valor a pagar: R${float(total_minutos*0.05)}") #0.05=3/60
else: 
    if total_horas<=2:
        print(f"Valor a pagar: R${float(total_horas*2.9+total_minutos*(2.9/60))}")
    else:
        print(f"Valor a pagar: R${float(total_horas*2.8+total_minutos*(2.8/60))}")
        
#Tô com sonooooooo, mecher na lógica
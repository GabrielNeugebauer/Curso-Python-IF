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
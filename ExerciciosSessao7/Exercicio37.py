
vetorA = []
nao_ordenados = []

print('Digite 11 números')

for i in range(11):
    numero = int(input(f'{i+1}º: '))
    if len(vetorA) <= 6:
        vetorA.append(numero)
        vetorA.sort()
    else:
        vetorA.append(numero)


print(vetorA)
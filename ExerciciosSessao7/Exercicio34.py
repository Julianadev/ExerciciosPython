
vetor = []

print('Digite 10 números: ')

for i in range(10):
    numero = int(input(f'{i+1}º: '))
    if numero in vetor:
        print('Número repetido, digite outro...')
    elif numero not in vetor:
        vetor.append(numero)
    else:
        print('Número inválido')

print(vetor)
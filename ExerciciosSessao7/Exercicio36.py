
vetor = []

print('Digite 10 números reais')

for _ in range(10):
    numero = float(input(f'{_+1}º: '))
    vetor.append(numero)

vetor.sort()

print(f'Vetor ordenado: {vetor}')
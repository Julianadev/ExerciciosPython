
vetor = []

print('Digite 10 valores númericos')

for _ in range(10):
    numero = int(input(f'{_+1}º: '))
    vetor.append(numero)

vetor.sort()

print(vetor)
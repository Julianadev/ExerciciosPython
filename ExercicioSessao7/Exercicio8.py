lista = []

print('Digite 6 números inteiros: ')

for _ in range(6):
    numeros = int(input())
    lista.append(numeros)

print(f'Lista: {lista}')
print(f'Lista em ordem reversa: {lista[::-1]}')
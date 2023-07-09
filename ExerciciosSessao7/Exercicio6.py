
lista = []

print('Digite 10 números: ')

for _ in range(10):
    numeros = int(input())
    lista.append(numeros)

print(f'Lista: {lista}')
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')

lista = []

print('Digite 10 números inteiros: ')

for _ in range(10):
    numeros = int(input())
    lista.append(numeros)

print(f'Lista: {lista}')
print(f'Maior número {max(lista)} posição: {lista.index(max(lista))}')
lista = []


print('Digite 5 números: ')

for _ in range(5):
    numeros = int(input())
    lista.append(numeros)


print(f'Lista: {lista}')
print(f'Maior número: {max(lista)} - posição: {lista.index(max(lista))}')
print(f'Menor número: {min(lista)} - posição: {lista.index(min(lista))}')

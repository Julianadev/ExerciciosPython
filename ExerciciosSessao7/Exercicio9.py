
lista = []
contador_pares = 0

print('Digite 6 números inteiros: ')

for _ in range(6):
    numeros = int(input())
    lista.append(numeros)
    if numeros % 2 == 0:
        contador_pares += 1

numeros_pares = [num for num in lista if num % 2 == 0]
numeros_pares_inversos = numeros_pares[::-1]

print(f'Lista: {lista}')
print(f'Lista de números pares: {contador_pares}')
print(f'Lista de números pares em ordem inversa: {numeros_pares_inversos}')
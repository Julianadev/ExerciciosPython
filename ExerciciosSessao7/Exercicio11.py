
lista = []
contador_pares = 0
contador_negativo = 0

print('Digite 10 números reais: ')

for _ in range(10):
    numeros = float(input())
    lista.append(numeros)
    if numeros % 2 == 0:
        contador_pares += 1
    if numeros < 0:
        contador_negativo += 1


print(f'Lista: {lista}')
print(f'Números pares: {contador_pares}')
print(f'Números negativos: {contador_negativo}')

lista = []
contador_pares = 0

print('Digite 10 números: ')

for _ in range(10):
    numeros = int(input())
    lista.append(numeros)
    if numeros % 2 == 0:
        contador_pares += 1


print(f'Lista com 10 posições: {lista}')
print(f'Total de números pares na lista: {contador_pares}')



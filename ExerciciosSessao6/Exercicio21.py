
numeros_pares = []
numeros_impares = []
numeros = []

print('Digite 2 números')

for _ in range(2):
    numero = int(input(f'{_+1}º: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    elif numero % 2 != 0:
        numeros_impares.append(numero)
    else:
        numeros.append(numeros)

print(f'Números pares: {numeros_pares} - Soma: {sum(numeros_pares)}')
print(f'Numeros ímpares: {numeros_impares} - Soma: {sum(numeros_impares)}')





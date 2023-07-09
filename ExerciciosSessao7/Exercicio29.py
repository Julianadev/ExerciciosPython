numeros_pares = []
numeros_impares = []

print('Digite 6 numeros inteiros: ')
for i in range(6):
    numero = int(input(f'{i+1}º: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    elif numero % 2 != 0:
        numeros_impares.append(numero)
    else:
        print('Número inválido!')

print(f'Números pares: {numeros_pares}')
print(f'Soma dos números pares: {sum(numeros_pares)}')
print(f'Números ímpares: {numeros_impares}')
print(f'Quantidade de números ímpares: {len(numeros_impares)}')

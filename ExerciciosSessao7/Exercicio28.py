V = []
V1 = []
V2 = []

print('Digite 10 números inteiros: ')

for i in range(10):
    numero = int ( input ( f'{i+1}º: ' ) )
    V.append(numero)

for numero in V:
    if numero % 2 != 0:
        V1.append(numero)
    elif numero % 2 == 0:
        V2.append(numero)

print(f'V = {V}')
print(f'Números ímpares = {V1}')
print(f'Números pares = {V2}')

lista = []
numeros_iguais = 0

print('Digite 10 números: ')

for _ in range(10):
    numero = int(input())
    lista.append(numero)

for numero in lista:
    if lista.count(numero) > 1:
        numeros_iguais += 1

print(f'Lista: {lista}')
print(f'Números iguais: {numeros_iguais}')
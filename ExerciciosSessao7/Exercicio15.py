
lista = []

print('Digite 10 números: ')

for _ in range(10):
    numero = int(input())
    lista.append(numero)

numeros_unicos = list(set(lista))

print(f'Lista: {numeros_unicos}')


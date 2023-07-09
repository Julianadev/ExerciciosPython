lista = []

print('Digite 10 números: ')

for _ in range(10):
    numero = int(input())
    if numero < 0:
        numero = 0
    lista.append(numero)

print(lista)
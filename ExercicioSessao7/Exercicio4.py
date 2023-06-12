
lista = []
soma = 0

print('Digite 8 números')
for _ in range(8):
    numeros = int(input())
    lista.append(numeros)

soma = lista[1] + lista[2]
print(f'A soma de X e Y na posição: 1 - {lista[1]} e 2 - {lista[2]} é {soma}')

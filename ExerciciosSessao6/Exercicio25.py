
soma = 0

for numero in range(1, 1000):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero

print( f'A soma é: {soma}')
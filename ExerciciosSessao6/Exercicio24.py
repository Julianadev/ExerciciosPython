
divisores = []

numero = int(input('Digite um número: '))
for _ in range(1, numero):
    if numero % _ == 0:
        divisores.append(_)

for num in divisores:
    print(num)

soma = sum(divisores)

print(f'Número: {numero} - soma: {soma}')

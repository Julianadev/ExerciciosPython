
while True:
    numero = int(input('Digite um número: '))
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        print(f'Primeiro multiplo: {numero}')
        break
    numero += 1
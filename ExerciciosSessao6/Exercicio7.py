"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média

"""

soma = 0
contador = 0

for _ in range(10):
    numero = int(input('Digite o número: '))
    if numero > 0:
        soma += numero
        contador += 1
if contador > 0:
    media = soma / 10
    print(f'A média dos inteiros positivos é: {media}')
else:
    print('Nenhum número inteiro positivo foi inserido.')

"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

numeros = []

for _ in range(10):
    numero = input('Digite o número: ')
    numeros.append(numero)


print(f'Números digitados: {numeros}')
print(f'Maior número: {max(numeros)}')
print(f'Menot número: {min(numeros)}')
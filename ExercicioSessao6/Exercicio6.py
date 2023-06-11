"""
Faça um programa que leia 10 inteiros e imprima
sua saída.

"""

soma = 0

for _ in range(10):
    numero = int(input('Digite o número: '))
    soma += numero
media = soma / 10

print(f'A soma dos números é: {soma} e a média é: {media}')
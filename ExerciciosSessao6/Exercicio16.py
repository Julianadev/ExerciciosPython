"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números
impares de 1 ate N em ordem decrescente.

"""

N = int(input(f'Digite um número: '))

print(f'Número {N} de 1 até {N} em ordem descrescente: ')
for num in range(N+1, -1, -1):
    if num % 2 != 0:
        print(num)
"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números
impares de 1 ate N em ordem crescente.

"""

N = int(input('Digite um número: '))

print(f'Número {N} de 1 até {N} em ordem crescente: ')
for num in range(1, N+1, 3):
        print(num)
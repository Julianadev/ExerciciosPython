"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
pares de 0 ate N em ordem decrescente.

"""

N = int(input('Digite um número: '))

print(f'Número digitado: {N} em ordem decrescente: ')
for num in range(0, N+1, 3):
    print(num)
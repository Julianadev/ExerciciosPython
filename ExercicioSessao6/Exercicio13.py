"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
pares de 0 ate N em ordem crescente.

"""

N = int(input('Digite um número'))

print('Número digitado: ', N, 'em ordem crescente')
for num in range(0, N+1, 2):
    print(num)
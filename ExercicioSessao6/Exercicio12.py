"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 ate N em ordem decrescente.
"""

N = int(input("Digite um número inteiro positivo: "))

print("Números naturais de 0 até", N, "em ordem decrescente:")
for num in range(N, -1, -1):
    print(num)

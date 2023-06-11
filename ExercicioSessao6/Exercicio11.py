"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 ate N em ordem crescente.
"""

numero = int(input('Digite um número inteiro positivo: '))

print("Números naturais de 0 até", numero, "em ordem crescente:")
for num in range(numero + 1):
    print(num)
"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
"""

lista = []

for _ in range(6):
    numero = int(input('Digite um número: '))
    lista.append(numero)

for valor in lista:
    print(valor)


"""
Faça um programa que leia um número e, caso ele
seja positivo, calcule e mostre:

- O número digitado ao quadrado
- A raiz quadrada do número digitado
"""
import math

numero = 40

if numero > 0:
    print(f'{numero}² = {numero.__pow__(2)}')
    print ( f'Raíz quadrada = {math.sqrt(numero):.2f}')
else:
    print(f'Número inválido')
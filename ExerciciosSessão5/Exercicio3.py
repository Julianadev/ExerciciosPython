"""
Leia um número real. Se o número for positivo
imprima a raiz quadrada. Do contrário, imprima
o número ao quadrado
"""
import math

numero = float(input('Digite um número: '))
if numero > 0:
    print(f'Raíz quadrada: {math.sqrt(numero):.2f}')
else:
    print(f'{numero}² = {numero.__pow__(2)}')
"""
Leia um número fornecido pelo usuário.
Se esse número for positivo, calcule a raiz
quadrada do número.Se o número for negativo ,
mostre uma mensagem dizendo que o número é inválido.
"""
import math

numero = int(input('Digite um número: '))

if numero > 0:
    print(f'Raíz quadrada de {numero} = {math.sqrt(numero):.2f}')
else:
    print(f'Número inválido')

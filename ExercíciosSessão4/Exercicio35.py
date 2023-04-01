"""
Sejam a e b os catetos de um triângulo , onde
a hipotenusa é obtida pela equação:
hipotenusa = raiz quadrada a² + b³. Faça um programa
que receba os valores de a e b e calcule o valor da hipotenusa
atráves da equação. Imprima o resultado dessa operação.

"""
import math

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))
hipotenusa = math.sqrt(a ** 2 + b ** 3)
print(f'{hipotenusa:.2f}')

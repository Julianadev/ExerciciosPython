import math

def calcular_hipotenusa(a, b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return f'{hipotenusa:.2f}'

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

print(f'O valor da hipotenusa de {a} + {b} é {calcular_hipotenusa(a, b)}')
"""
Faça um programa que receba 2 números e mostre qual
é o maior deles
"""

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 < numero2:
    print(f'Número 2 é maior que número 1')
elif numero1 == numero2:
    print(f'Número 1 é igual a número 2')
else:
    print(f'Número 1 é maior que número 2')
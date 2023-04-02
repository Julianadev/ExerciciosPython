"""
Faça um programa que receba 2 números e mostre o maior
Se por caso, os dois números forem iguais , imprima a mensagem
"Numeros iguais".
"""

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 < numero2:
    print(f'{numero2} é maior que {numero1}')
elif numero1 == numero2:
    print('Números iguais')
else:
    print('Número inválido')
"""
Escreva um programa que, dados dois números inteiros,
mostre na tela o maior dels, assim como a diferença existente entre ambos.
"""

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
diferenca = numero1 - numero2

if numero1 > numero2:
    print(f'O primeiro é maior que o segundo')
else:
    print(f'Segundo é maior que o primeiro')

print(f'A diferença entre {numero1} e {numero2} é de: {diferenca}')

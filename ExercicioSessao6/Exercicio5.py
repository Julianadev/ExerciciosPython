"""
Faça um programa que peça ao usuário para digitar
10 valores e some-os.
"""

soma = 0

for n in range(10):
    valor = int(input('Digite o número: '))
    soma += valor
    print(soma)

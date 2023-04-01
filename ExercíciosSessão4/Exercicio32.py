"""
Leia um número inteiro e imprima a soma do sucessor
de seu triplo com o antecessor de seu dobro.
"""

numero = int(input('Digite um número: '))
triplo = numero*3
dobro = numero*2
sucessor = triplo + 1
antecessor = dobro - 1
soma = sucessor + antecessor
print(f'A soma do sucessor de seu triplo com o antecessor de seu dobro é: {soma}')
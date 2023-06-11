"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares.
"""

N = int(input('Digite um número inteiro: '))

num_impares = []

num = 1
while len(num_impares) < N:
    if num % 2 != 0:
        num_impares.append(num)
    num += 1

print("Os primeiros", N, "números naturais ímpares são: ")
for numero in num_impares:
    print(numero)
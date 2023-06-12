"""
Faça um programa que leia um número inteiro positivo n e calcule a soma dos
n primeiros números naturais.

"""
soma = 0

n = int(input('Digite um número: '))
for i in range(1, n+1):
    soma += i

print(f"A soma dos {n} primeiros números naturais é: {soma}")


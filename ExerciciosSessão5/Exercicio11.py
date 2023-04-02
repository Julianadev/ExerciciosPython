"""
Escreva um programa que leia um número inteiro
maior do que zero e devolva, na tela, a soma de todos
os Seus algarismos. por exemplo, ao número 251 corresponderá
0 valor 8 (2 + 5 + 1). Se o número lido não for maior que zero,
o programa terminará com a mensagem "Número inválido".
"""


num = int(input("Digite um número inteiro maior que zero: "))
if num > 0:
    soma = 0
    for digito in str(num):
        soma += int(digito)
    print(f"A soma dos algarismos de {num} é {soma}.")
else:
    print("Número inválido.")
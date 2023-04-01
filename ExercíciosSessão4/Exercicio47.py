"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha
"""

numero = int(input('Digite um número inteiro de 1000 a 9999: '))

if 1000 <= numero <= 9999:
    print(numero // 1000)
    print((numero // 100) % 10)
    print((numero // 10) % 10)
    print(numero % 10)
else:
    print('O número deve estar entre 1000 e 9999')
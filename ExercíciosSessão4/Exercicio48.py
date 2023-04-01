"""
Leia um valor inteiro em segundos e imprima-o em horas,
minutos e segundos
"""

numero = int(input('Digite um número inteiro: '))
horas = numero // 3600
numero %= 3600
minutos = numero // 60
numero %= 60
print(f'{horas} horas, {minutos} minutos, {numero} segundos')
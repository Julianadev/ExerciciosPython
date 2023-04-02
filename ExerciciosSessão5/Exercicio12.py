"""
Ler um número inteiro. Se 0 número lido for negativo, escreva a mensagem "Número
inválido". Se 0 número positivo, calcular o logaritmo deste numero

"""
import math

numero = int(input('Digite um número inteiro: '))

if numero > 0:
    logaritmo = math.log(numero)
    print(f'O logaritmo de {numero} é {logaritmo:.2f}')
else:
    print('Número inválido')
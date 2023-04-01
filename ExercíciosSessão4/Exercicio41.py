"""
Faça um programa que leia o valor da hora
de trabalho(em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser
pago ao funcionário, adicionando 10% sobre
o valor calculado
"""

valor_da_hora = float(input('Digite o valor da hora de trabalho em reais: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas: '))
salario = valor_da_hora * horas_trabalhadas
acrescimo = salario * 1.10
print(f'O valor a ser pago ao funcionário é: R$ {acrescimo:.2f}'.replace('.', ','))

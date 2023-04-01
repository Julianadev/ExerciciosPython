"""
Leia o salário de um funcionário.Calcule e
imprima o valor do novo salário, sabendo que ele
recebeu um aumento de 20%
"""

salario = float(input('Digite seu salário: '))
aumento = salario/100*20
novo_salario = salario + aumento
print(f'Seu novo salário é: R$ {novo_salario:.2f}'.replace('.', ','))

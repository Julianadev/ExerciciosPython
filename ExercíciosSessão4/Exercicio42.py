"""
Receba o salário de um funcionário.
Calcule e imprima o salário a receber, sabendo-se
que o funcionario tem uma gratificação de 5% sobre o salário-base.
Além disso ele 7% de imposto sobre o salário-base.
"""

salario = float(input('Digite seu salário: '))
gratificacao = salario/100 * 5
descontos = salario/100 * 7
salario_liquido = salario + gratificacao - descontos
print(f'Salário base: {salario}')
print(f'Gratificação: {gratificacao}')
print(f'Desconto de 7% imposto de renda: {descontos}')
print(f'Salário líquido: {salario_liquido:.2f}'.replace('.', ','))

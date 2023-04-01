"""
Uma empresa contrata um encanador a R$ 30,00
p/dia. Faça um programa que solicite o número
de dias trabalhados pelo encanador e imprima
a quantia líquida que deverá ser paga, sabendo-se
que são descontados 8% para imposto de renda.
"""
print('---------------Calculadora Salarial-------------------')
diasTrabalhados = int(input('Digite quantos dias você trabalhou: '))
salario = 30*diasTrabalhados
descontos = salario/100*8
liquido = salario - descontos
print(f'Sálario Bruto: R$ {salario:.2f}'.replace('.', ','))
print(f'8% imposto de renda: R$ {descontos:.2f}'.replace('.', ','))
print(f'Sálario líquido: R$ {liquido:.2f}'.replace('.', ','))

"""
Implemente um programa que calcule o ano de nascimento de
uma pessoa a partir de sua idade e do ano atual.
"""

idade = int(input('Digite sua idade: '))
ano_atual = int(input('Digite o ano atual, Se você ainda não tiver feito aniversário este ano digite o ano anterior: '))
ano_nascimento = ano_atual - idade
print(f'Você nasceu em {ano_nascimento}')

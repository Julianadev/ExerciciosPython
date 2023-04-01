"""
Faça um programa que leia um número inteiro
positivo de tres dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos
do número lido. Exemplo:
NumeroLido = 123
NumeroGerado = 321
"""
numero_lido = int(input("Digite um número inteiro positivo de três dígitos (de 100 a 999): "))
centena = numero_lido // 100
dezena = (numero_lido % 100) // 10
unidade = numero_lido % 10
numero_gerado = unidade * 100 + dezena * 10 + centena
print(f"O número gerado é: {numero_gerado}")
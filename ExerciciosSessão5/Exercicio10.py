"""
Faça um programa que receba a altura e o sexo
de uma pessoa e calcule e mostre seu peso
ideal, utilizando as seguintes fórmulas(onde h corresponde
à altura)
"""
altura = float(input('Digite sua altura: '))
sexo = input("Digite seu sexo (M/F): ")

if sexo == "M" or "m":
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é:", round(peso_ideal, 2), "kg")
elif sexo == "F" or "f":
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é:", round(peso_ideal, 2), "kg")
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")
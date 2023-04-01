"""
Receba a altura do degrau de uma escada e a altura
que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuário deverá
subir para atingir seu objetivo.
"""

degrau = float(input('Digite a altura do degrau: '))
altura = float(input('Digite a altura que você deseja alcançar: '))
meta = altura / degrau
print(meta)
"""
Escreva um programa que leia as coordenadas
x e y de pontos no R² e calcule sua distância
da origem ( 0 , 0).
"""
import math

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))
distancia = math.sqrt(x**2 + y**2)
print(f'A distância da posição ({x},{y}) para a origem (0,0) é {distancia:.2f}')
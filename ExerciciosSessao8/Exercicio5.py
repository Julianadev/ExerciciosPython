import math

def volume_esfera(raio):
    v = (4 / 3) * math.pi * raio**3
    return f'{v:.2f}'

def programa_teste():
    raio = float(input('Digite o raio: '))
    volume = volume_esfera(raio)
    print(f'O volume da esfera com raio {raio} é: {volume}')

programa_teste()
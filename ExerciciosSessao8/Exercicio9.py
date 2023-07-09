import math


def volume_cilindro(altura, raio):
    V = math.pi * raio ** 2 * altura
    return f'{V:.2f}'



altura = float(input('Digite a altura: '))
raio = float(input('Digite o valor do raio: '))

print(f'O valor de um cilindro circular é: {volume_cilindro(altura, raio)}')
"""
Leia a altura e o raio de um cilindro circular e
imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio
da seguinte fórmula: V = PI * raio² * altura
"""

altura = 12
raio = 4
volume = 3.141592*raio.__pow__(2)*altura
print(f'{volume:.2f}')

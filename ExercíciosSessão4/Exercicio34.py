"""
Leia o valor do raio de um círculo e
calcule e imprima a área do círculo
correspondente. A área do círculo é PI * raio²,
considere PI = 3.14
"""
raio_circulo = 40
area = 3.141592*raio_circulo.__pow__(2)
print(f'O raio do círculo é: {area:.2f}'.replace('.', ','))

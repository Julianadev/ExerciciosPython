
import math

def quadrado_perfeito(numero):
    raiz = math.isqrt(numero)
    return raiz * raiz == numero


numero = int(input('Digite um número: '))
if quadrado_perfeito(numero):
    print(f'O {numero} é quadrado perfeito')
else:
    print(f'O {numero} não é quadrado perfeito')


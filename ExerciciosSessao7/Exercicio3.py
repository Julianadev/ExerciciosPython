"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.

"""

conjunto_original = []
for i in range(10):
    numero = float(input("Digite um número real: "))
    conjunto_original.append(numero)


conjunto_quadrado = []
for numero in conjunto_original:
    quadrado = numero ** 2
    conjunto_quadrado.append(quadrado)


print("Conjunto original:")
for numero in conjunto_original:
    print(numero)

print("Conjunto com os quadrados:")
for quadrado in conjunto_quadrado:
    print(quadrado)





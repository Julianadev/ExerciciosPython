
vetor = []

print("Digite os elementos do vetor (15 elementos): ")
for _ in range(15):
    numero = int(input(f'{_+1}º: '))
    vetor.append(numero)


indice_destino = 0

for indice_origem in range(len(vetor)):
    if vetor[indice_origem] != 0:
        vetor[indice_destino] = vetor[indice_origem]
        indice_destino += 1

for i in range(indice_destino, len(vetor)):
    vetor[i] = 0

print("Vetor compactado:", vetor)

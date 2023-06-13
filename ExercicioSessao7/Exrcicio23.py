

print('Digite os números do primeiro vetor ')
vetor1 = []
for i in range(5):
    numero = int(input(f'Digite o {i+1}º: '))
    vetor1.append(numero)

print('\nDigite os números para o segundo vetor ')
vetor2 = []
for i in range(5):
    numero = int(input(f'Digite o {i+1}º: '))
    vetor2.append(numero)

produto = 0
for i in range(5):
    produto += vetor1[i] * vetor2[i]

print(f'\nPrimeiro conjunto: {vetor1}')
print(f'Segundo conjunto: {vetor2}')
print(f'Produto escalar: {produto}')


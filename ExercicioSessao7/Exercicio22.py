vetor1 = []
vetor2 = []
vetor3 = []
posicao_par = 0
posicao_impar = 0

print('Digite 10 números para o primeiro vetor')
for i in range(10):
    numero = int(input(f'Digite o {i+1}º : '))
    vetor1.append(numero)

print('Digite 10 números para o segundo vetor')
for i in range(10):
    numero = int(input(f'Digite o {i+1}º : '))
    vetor2.append(numero)


for num1, num2 in zip(vetor1, vetor2):
    if num1 % 2 == 0:
        vetor3.append(num1)
        posicao_par += 1
    elif num2 % 2 != 0:
        vetor3.append(num2)
        posicao_impar += 1
    else:
        vetor3.append ( num1 )
        posicao_impar += 1

print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Vetor 3: {vetor3}')
print(f'Vetor 3 posição par: {posicao_par}')
print(f'Vetor 3 posição ímpar: {posicao_impar}')
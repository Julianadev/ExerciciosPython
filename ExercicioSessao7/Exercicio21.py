A = []
B = []

print('Digite os números do primeiro vetor: ')

for _ in range(10):
    numero = int(input())
    A.append(numero)

print('Digite os números do segundo vetor: ')

for _ in range(10):
    numero = int(input())
    B.append(numero)

C = list(A + B)

print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')
primeiro_vetor = []
segundo_vetor = []

for i in range(10):
    while True:
        numero = int(input(f"Digite o {i+1}º número inteiro entre 1 e 50: "))
        if numero > 0 and numero <= 50:
            primeiro_vetor.append(numero)
            break
        else:
            print("Número inválido. Digite um número inteiro entre 1 e 50.")


for numero in primeiro_vetor:
    if numero % 2 != 0:
        segundo_vetor.append(numero)

print("Primeiro vetor:")
for i in range(0, len(primeiro_vetor), 2):
    print(primeiro_vetor[i], primeiro_vetor[i+1])

print("\nSegundo vetor:")
for i in range(0, len(segundo_vetor), 2):
    if i+1 < len(segundo_vetor):
        print(segundo_vetor[i], segundo_vetor[i+1])
    else:
        print(segundo_vetor[i])

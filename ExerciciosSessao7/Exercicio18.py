vetor = []

print("Digite 10 números:")

for _ in range(10):
    numero = int(input())
    vetor.append(numero)

x = int(input("Digite um número inteiro X: "))

multiplos = [num for num in vetor if num % x == 0]

print("Vetor:")
print(vetor)
print(f"Números múltiplos de {x}:")
print(multiplos)

contador_maior = 0
maior_numero = 0

quantidade = int(input("Digite a quantidade de números a serem lidos: "))
for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    if numero > maior_numero:
        maior_numero = numero
        contador_maior = 1
    elif numero == maior_numero:
        contador_maior += 1

print(f"O maior número é: {maior_numero}")
print(f"Ele foi lido {contador_maior} vezes.")


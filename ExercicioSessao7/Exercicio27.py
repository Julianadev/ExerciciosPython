vetor = []

while True:
    numero = int(input("Digite um número (digite 0 para sair): "))

    if numero == 0:
        break

    if numero <= 1:
        primo = False
    else:
        primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break

    if primo:
        vetor.append(numero)
        print(f'O número {numero} é primo.')
    else:
        print(f'O número {numero} não é primo.')

print(f'Vetor: {vetor}')

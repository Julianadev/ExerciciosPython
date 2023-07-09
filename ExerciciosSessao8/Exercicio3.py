
def positivo_negativo():
    numero = int(input('Digite um número: '))
    if numero >0:
        return 1
    elif numero <0:
        return -1
    elif numero == 0:
        return 0
    else:
        return f"Número inválido!"

print(positivo_negativo())

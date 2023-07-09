
def qual_numero_maior(lista):
    return(max(lista))

lista = []
for i in range(2):
    numero = int(input(f'Digite o {i+1}º número: '))
    lista.append(numero)

print(f'Maior número: {qual_numero_maior(lista)}')
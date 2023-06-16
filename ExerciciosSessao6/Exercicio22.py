
lista = []

print('Digite as notas entre 10 a 20: ')

while True:
    nota = float(input())
    if nota < 10 or nota > 20:
        break
    lista.append(nota)

if len(lista) > 0:
    media = sum(lista) / len(lista)
    print(f'A média das notas é {media:.2f}')
else:
    print('Nenhuma nota válida foi inserida.')
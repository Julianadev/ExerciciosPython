
lista = []

for i in range(1, 101):
    lista.append(i)

multiplos = [i for i in lista if i % 7 != 0 and str(i)[-1] != '7']

print(f'Lista: {lista}')
print(f'Números não múltiplos de 7 e que não terminam em 7:  {multiplos}')


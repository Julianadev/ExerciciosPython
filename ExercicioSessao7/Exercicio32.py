v1 = []
v2 = []

print('Digite 5 números inteiros para o primeiro vetor: ')

for i in range(5):
    numero = int(input(f'{i+1}º: '))
    v1.append(numero)

for i in range(5):
    numero = int ( input ( f'{i + 1}º: ' ) )
    v2.append ( numero )

soma = []
for i in range(5):
    soma.append(v1[i] + v2[i])

produto = []
for i in range(5):
    produto.append(v1[i]*v2[i])


diferenca = []
for numero in v1:
    if numero not in v2:
        diferenca.append(numero)

intersecao = []
for numero in v1:
    if numero in v2:
        intersecao.append(numero)

uniao = v1.copy()
for numero in v2:
    if numero not in v1:
        uniao.append(numero)

print(f'Soma de cada elemento de v1 e v2 na mesma posição: {soma}')
print(f'Produto da multiplição entre v1 e v2 na mesma posição: {produto}')
print(f'Diferença: {diferenca}')
print(f'Interseção: {intersecao}')
print(f'União: {uniao}')

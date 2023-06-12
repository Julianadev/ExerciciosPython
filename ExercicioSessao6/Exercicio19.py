"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o número de dados lidos e número de valores pares.
O processo termina quando for digitado o número 1000.

"""

contador = 0
contador_pares = 0

print('Digite os números ou então digite 1000 para sair')

while True:
    numero = int(input())
    if numero == 1000:
        break
    contador += 1
    
    if numero % 2 == 0:
        contador_pares += 1

print(f'Total de números lidos: {contador}')
print(f'Total de números pares: {contador_pares}')
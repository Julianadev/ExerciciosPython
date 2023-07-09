lista = [2.3, 8.5, 3.3, 10.2, 6.5]

print('Escolha uma opção: ')
print('[1] - Ordem direta')
print('[2] - Ordem inversa')
print('[0] - Sair')


while True:
    opcao = int ( input ( ) )
    if opcao == 0:
        break
    elif opcao == 1:
        print(lista)
    elif opcao == 2:
        print(lista[::-1])
    else:
        print('Opção inválida')

for numero in lista:
    inteiro = int(numero)
    print(inteiro)
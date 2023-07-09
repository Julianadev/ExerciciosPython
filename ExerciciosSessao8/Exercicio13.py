
def calculadora(numero1, numero2, simbolo):
    if simbolo == '+':
        resultado = int(numero1 + numero2)
        return resultado
    elif simbolo == '-':
        resultado = int(numero1 - numero2)
        return resultado
    elif simbolo == '/':
        resultado = int(numero1 / numero2)
        return resultado
    elif simbolo == '*':
        resultado = int(numero1 * numero2)
        return resultado
    return 'Opção inválida'



print('Escolha a operação que deseja realizar: ')
print('[ + ] - Soma')
print('[ - ] - Subtração')
print('[ / ] - Divisão')
print('[ * ] - Multiplicação')

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
simbolo = input('Digite a operação que deseja realizar: ')

print(f'Resultado: {calculadora(numero1, numero2, simbolo)}')


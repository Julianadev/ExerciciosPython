
def soma_numeros(numero):
    if numero > 0:
        digitos = [int(digito) for digito in str(numero)]
        return sum(digitos)
    return 'Número inválido'



numero = int(input('Digite um número inteiro maior que 0: '))
print(f'A soma é {soma_numeros(numero)}')


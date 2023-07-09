
def eh_triangulo(n1, n2, n3):
    if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
        return 'É um triângulo'
    return 'Não é um triângulo'

def tipo_de_triangulo(n1, n2, n3):
    if n1 == n2 == n3:
        return 'Equilátero'
    elif n1 == n2 or n1 == n3 or n2 == n3:
        return 'Isósceles'
    else:
        return 'Escaleno'



n1 = float(input('Digite o primeiro número maior que 0: '))
n2 = float(input('Digite o segundo número maior que 0: '))
n3 = float(input('Digite o terceiro número maior que 0: '))


print(eh_triangulo(n1, n2, n3))
print(tipo_de_triangulo(n1, n2, n3))
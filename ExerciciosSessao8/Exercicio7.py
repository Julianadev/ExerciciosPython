
def graus_fahrenheit(C):
    fahrenheit = C * (9.0/5.0) + 32.0
    return f'{fahrenheit:.2f}'

C = float(input('Digite a temperatura: '))
print(f'A temperatura convertida para Fahrenheit é: {graus_fahrenheit(C)}')
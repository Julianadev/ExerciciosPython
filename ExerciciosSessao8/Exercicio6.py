
def converter_para_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos



horas = int(input('Digite a hora: '))
minutos = int(input('Digite o minuto: '))
segundos = int(input('Digite os segundos: '))

resultado = converter_para_segundos(horas, minutos, segundos)

print(f'O total de segundos é: {resultado}')

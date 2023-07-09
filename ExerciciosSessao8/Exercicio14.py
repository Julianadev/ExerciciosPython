
def calculo_economia_carro(distancia, litro):
    resultado = litro / distancia
    if resultado < 8:
        return f' Consumo: {resultado:.2f} km/l - Venda o carro!'
    elif resultado > 8 and resultado < 14:
        return f'Consumo: {resultado:2f} km/l - Econômico!'
    elif resultado > 12:
        return f'Consumo: {resultado:2f} km/l - Super econômico!'


distancia = float(input('Digite a distância: '))
litro = float(input('Digite o litro: '))

print(f'O resultado é: {calculo_economia_carro(distancia, litro)}')
import locale
from datetime import datetime

def exibir_data_por_extenso(dia, mes, ano):
    try:
        data = datetime(year=ano, month=mes, day=dia)
        locale.setlocale(locale.LC_TIME,'pt-BR.UTF-8')
        data_formatada = data.strftime("%d de %B de %Y")
        return data_formatada
    except ValueError:
        return "Data inválida"

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

data_extenso = exibir_data_por_extenso(dia, mes, ano)

print(data_extenso)


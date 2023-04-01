"""
Leia um valor em real e a cotação do dólar.
Em seguida , imprima o valor correspondente em
dólares.
"""
real = float(input("Digite o valor em reais: "))
dolar = float(input("Digite a cotação do dólar: "))
conversao = real/dolar
print(f' ${conversao:.2f}')

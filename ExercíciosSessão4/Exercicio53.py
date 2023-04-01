"""
Faça um programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preço do
metro de tela p . Imprima o custo para cercar este
mesmo terreno com tela.
"""

def fencing_cost(length, width, price_per_meter):
    perimeter = 2 * (length + width)
    total_cost = perimeter * price_per_meter
    print(f"Dimensões do terreno: {total_cost:.2f}")


length = 10
width = 20
price_per_meter = 5
fencing_cost(length, width, price_per_meter)
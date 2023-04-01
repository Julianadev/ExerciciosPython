"""
Escreva um programa de ajuda para vendedores.
A partir de um valor total lido. Mostre:

- O total a pagar com desconto de 10%;
- O valor de cada parcela, no parcelamento de 3x sem juros;
- A comissão do vendedor, no caso da venda ser a vista
(5% sobre p valor com desconto)
- A comissão do vendedor , no caso da venda ser parcelada
(5% sobre o valor total)

"""

valor_compra = float(input('Digite o valor da compra: '))
desconto = valor_compra/100*10
total_com_desconto = valor_compra - desconto
valor_parcela = valor_compra/3
comissao_vendedor_avista = total_com_desconto*0.05
comissao_vendedor_parcelada = valor_compra*0.05

print(f'Valor da compra: R$ {valor_compra:.2f}'.replace('.', ','))
print(f'Desconto: R$ {desconto:.2f}'.replace('.', ','))
print(f'Total com desconto: R$ {total_com_desconto:.2f}'.replace('.', ','))
print(f'Valor da parcela, 3x sem juros: R$ {valor_parcela:.2f}'.replace('.', ','))
print(f'Comissão recebida venda à vista: (5% sobre o valor total) - R$ {comissao_vendedor_avista:.2f}'.replace('.', ','))
print(f'Comissão recebida venda parcelada: (5% sobre o valor total) -  R$ {comissao_vendedor_parcelada:.2f}'.replace('.', ','))
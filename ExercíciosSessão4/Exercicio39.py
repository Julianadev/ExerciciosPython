"""
A importância de R$ 780.000,00 será dividida
entre 3 ganhadores de um concurso. Sendo que da
quantia total:

- O primeiro ganhador receberá 46%
- O segundo receberá 32%
- O terceiro receberá o restante

Calcule e imprima a quantia ganha por cauda
um dos ganhadores.
"""

premio = 780000.00
primeiro_ganhador = premio*0.46
segundo_ganhador = premio*0.32
terceiro_ganhador = premio - primeiro_ganhador - segundo_ganhador
print(f'Ganhador 1 prêmio: {primeiro_ganhador:.2f}'.replace('.', ','))
print(f'Ganhador 2 prêmio: {segundo_ganhador:.2f}'.replace('.', ','))
print(f'Ganhador 3 prêmio: {terceiro_ganhador:.2f}'.replace('.', ','))

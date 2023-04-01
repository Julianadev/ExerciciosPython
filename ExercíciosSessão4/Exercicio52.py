"""
Três amigos jogaram na loteria. Caso eles
ganhem o prêmio deve ser repartido proporcionalmente
ao valor que cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com
base no valor investido.
"""
premio = float(input('Digite o valor do premio: '))
apostador1 = float(input('Digite o valor que você apostou: '))
apostador2 = float(input('Digite o valor que você apostou: '))
apostador3 = float(input('Digite o valor que você apostou: '))

totalInvestido = apostador1 + apostador2 + apostador3

proporcao_amigo1 = apostador1 / totalInvestido
proporcao_amigo2 = apostador2 / totalInvestido
proporcao_amigo3 = apostador3 / totalInvestido

valor_amigo1 = proporcao_amigo1*premio
valor_amigo2 = proporcao_amigo2*premio
valor_amigo3 = proporcao_amigo3*premio

print(f'O Amigo 1 deve receber R$ {valor_amigo1:.3f}')
print(f'O Amigo 2 deve receber R$ {valor_amigo2:.3f}')
print(f'O Amigo 3 deve receber R$ {valor_amigo3:.3f}')

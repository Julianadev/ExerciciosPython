aluno_mais_alto = 0
altura_mais_alta = 0
aluno_mais_baixo = 0
altura_mais_baixa = float('inf')

for i in range(10):
    numero_aluno = int(input(f'Digite o número do {i+1}º aluno: '))
    altura_aluno = float(input(f'Digite a altura do {i+1}º aluno '))

    if altura_aluno > altura_mais_alta:
        aluno_mais_alto = numero_aluno
        altura_mais_alta = altura_aluno

    if altura_aluno < altura_mais_baixa:
        aluno_mais_baixo = numero_aluno
        altura_mais_baixa = altura_aluno


print(f'Aluno mais baixo: {aluno_mais_baixo} - Altura: {altura_mais_baixa}')
print(f'Aluno mais alto: {aluno_mais_alto} - Altura: {altura_mais_alta}')
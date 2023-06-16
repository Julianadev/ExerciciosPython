
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

peso1 = 1
peso2 = 1
peso3 = 2

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f'Média do aluno: {media:.2f}')

if media > 60:
    print('Aluno aprovado!')
else:
    print('Aluno Reprovado')
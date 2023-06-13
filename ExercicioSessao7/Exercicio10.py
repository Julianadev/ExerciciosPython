
notas = []
soma = 0

print('Digite a nota dos 15 alunos: ')

for _ in range(15):
    nota = float(input())
    notas.append(nota)
    soma += nota

media = soma / 15

print(f'Notas: {notas}')
print(f'A soma das notas é: {soma:.2f} e a média é {media:.2f}')
def nota_aluno(nota1, nota2, nota3, letra):
    lista = [nota1, nota2, nota3]
    if letra == 'A':
        media_aritmetica = sum(lista) / len(lista)
        return f'{media_aritmetica:.2f}'
    elif letra == 'P':
        media_poderada = (nota1 * 5 + nota2 * 3 +nota3 * 2) / 10
        return f'{media_poderada:.2f}'
    else:
        return 'Opção inválida'



print('Digite a nota do aluno e as opções abaixo')
print('[A] - Calcular média aritmética')
print('[P] - Calcular média ponderada ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
letra = input('Digite a opção escolhida: ').upper()

print(f'Cálculo = {nota_aluno(nota1, nota2, nota3, letra)}')



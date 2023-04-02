"""
Faça um programa que leia 2 notas de um aluno,
verifique se as notas são validas e exiba na tela a média
destas notas. Uma nota válida deve ser, obrigatoriamente,
um valor entre 0.0 e 10.0, onde caso a nota não possua
um valor válido, este fato deve ser informado
ao usuário e o programa termina
"""

nota1 = float(input('Digite a nota do primeiro aluno (0 a 10): '))
nota2 = float(input('Digite a nota do segundo aluno (0 a 10): '))
media = nota1 + nota2 / 2

if nota1 < 0.0 or nota1 > 10.0:
    print ( "Nota inválida! A nota deve estar entre 0.0 e 10.0." )
    quit ( )

if nota2 < 0.0 or nota2 > 10.0:
    print ( "Nota inválida! A nota deve estar entre 0.0 e 10.0." )
    quit ( )

print(f'Média dos alunos: {media}')
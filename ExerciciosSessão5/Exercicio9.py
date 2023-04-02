"""
Leia o salário de um trabalhador e o valor
da prestação de um empréstimo. Se a prestação for maior
que 20% do salário imprima: "Empréstimo não
concedido" , caso contrário imprima: "Empréstimo concedido"
"""

salario = float(input('Digite o valor do seu salário: '))
emprestimo_valor = float(input('Digite o valor do empréstimo: '))

if emprestimo_valor > salario * 0.2:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
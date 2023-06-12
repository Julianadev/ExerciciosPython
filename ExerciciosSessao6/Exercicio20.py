"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número

"""
numero = int ( input ( "Digite um número inteiro entre 100 e 999: " ) )


if numero < 100 or numero > 999:
    print ( "Número inválido!" )
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    print ( "Centenas:", centenas )
    print ( "Dezenas:", dezenas )
    print ( "Unidades:", unidades )

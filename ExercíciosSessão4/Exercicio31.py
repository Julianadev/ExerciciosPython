"""
Leia um número inteiro e imprima o seu antecessor
e o seu sucessor
"""
numero = int ( input ( 'Digite um número: ' ) )
antecessor = numero - 1
sucessor = numero + 1
print ( f'Seu número: {numero} <- Antecessor: {antecessor} - Sucessor -> {sucessor}' )

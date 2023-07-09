
n = int ( input ( "Digite um número inteiro positivo: " ) )


triangulo = [ ]
for linha in range ( n ):

    linha_atual = [ 1 ]


    for i in range ( 1, linha ):
        valor = triangulo[ linha - 1 ][ i - 1 ] + triangulo[ linha - 1 ][ i ]
        linha_atual.append ( valor )


    if linha > 0:
        linha_atual.append ( 1 )

    triangulo.append ( linha_atual )


for linha in triangulo:
    for valor in linha:
        print ( valor, end=" " )
    print ( )

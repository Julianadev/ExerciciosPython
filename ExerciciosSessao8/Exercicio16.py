def DesenhaLinha(sinais):
    simbolo = input('Digite o símbolo: ')
    linha = simbolo * sinais
    return linha

sinais = int(input('Digite quantos sinais serão mostrados: '))
print(DesenhaLinha(sinais))

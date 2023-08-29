
with open('texto.txt', 'w', encoding='UTF-8') as arquivo:
    conteudo = input('Digite o texto: ')
    arquivo.write(conteudo)
print('Arquivo criado com sucesso.')

with open('texto.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    numero_de_linhas = len(linhas)
    print(f'O arquivo possui {numero_de_linhas} linhas')
primeiro_arquivo = input('Digite o nome do primeiro arquivo: ')
segundo_arquivo = input('Digite o nome do segundo arquivo: ')
terceiro_arquivo = input('Digite um nome para o terceiro arquivo modificado: ')

try:
    with open(primeiro_arquivo, 'r') as arquivo1, open(segundo_arquivo, 'r') as arquivo2:
        conteudo1 = arquivo1.read()
        conteudo2 = arquivo2.read()

    conteudo_combinado = f'{conteudo1} \n{conteudo2}'

    with open(terceiro_arquivo, 'w', encoding='UTF-8') as arquivo3:
        arquivo3.write(conteudo_combinado)

    print('Conteúdo modificado com sucesso!')
except FileNotFoundError:
    print('Arquivo não encontrado!')
except Exception as e:
    print('Ocorreu um erro: ', e)

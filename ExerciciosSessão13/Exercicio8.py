nome_arquivo_entrada = input('Digite o nome do arquivo: ')

try:
    with open(nome_arquivo_entrada, 'r') as arquivo:
        conteudo = arquivo.read()
        conteudo_modificado = ''.join([caractere.lower() for caractere in conteudo])
    nome_arquivo_saida = input('Digite o novo nome do arquivo: ')
    with open(nome_arquivo_saida, 'w', encoding='UTF-8') as arquivo:
        arquivo.write(conteudo_modificado)
    print('Arquivo modificado com sucesso!')
except FileNotFoundError:
    print('Arquivo não encontrado!')
except Exception as e:
    print('Ocorreu um erro: ', e)

abrindo_arquivo = input('Deseja abrir o arquivo modificado? S/N ')
if abrindo_arquivo.upper() == 'S':
    with open(nome_arquivo_saida, 'r') as arquivo:
        print(arquivo.read())
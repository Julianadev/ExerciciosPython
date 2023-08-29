def eh_vogal(caractere):
    vogais = 'AEIOUaeiou'
    if caractere in vogais:
        return '*'
    else:
        return caractere

nome_arquivo = input('Digite o nome do seu arquivo: ')

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        conteudo_modificado = ''.join([eh_vogal(caractere) for caractere in conteudo])
    novo_nome_arquivo = input('Digite o nome do arquivo de saída: ')

    with open(novo_nome_arquivo, 'w', encoding='UTF-8') as arquivo:
        arquivo.write(conteudo_modificado)
    print('Arquivo modificado com sucesso!')
except FileNotFoundError:
    print('Arquivo não encontrado!')
except Exception as e:
    print('Ocorreu um erro: ', e)

abrindo_arquivo = input('Deseja abrir o arquivo modificado? S/N ')
if abrindo_arquivo.upper() == 'S':
    try:
        with open(novo_nome_arquivo, 'r') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print('Arquivo não encontrado!')
else:
    print('Encerrando o programa')
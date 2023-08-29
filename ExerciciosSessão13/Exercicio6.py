from collections import Counter

nome_arquivo = input('Digite o nome do seu arquivo: ')

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        conteudo_sem_espacos = conteudo.replace(' ','')
        contagem = Counter(conteudo_sem_espacos)
        print(f'O arquivo possui: {contagem} no arquivo')
except FileNotFoundError:
    print('Arquivo não foi encontrado')
except Exception as e:
    print('Ocorreu um erro: ', e)
    
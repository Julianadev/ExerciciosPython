from collections import Counter


nome_arquivo = input('Digite o nome do arquivo: ')
palavra = input('Digite a palavra que deseja realizar a contagem: ')


try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        contagem = Counter(palavras)
        frequencia = contagem.get(palavra, 0)
        print(f'A palavra {palavra} aparece {frequencia}x no arquivo')
except FileNotFoundError:
    print('Arquivo não encontrado!')
except Exception as e:
    print('Ocorreu um erro: ', e)


from collections import Counter

texto = input('Digite o nome do arquivo: ')
caractere = input('Digite o caractere: ')


try:
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        contagem_caractere = Counter(conteudo)
        resultado = contagem_caractere[caractere]
        print(f'O caractere {caractere} aparece {resultado}x no arquivo.')
except FileNotFoundError:
    print('Arquivo não encontrado.')
except Exception as e:
    print('Ocorreu um erro: ', e)
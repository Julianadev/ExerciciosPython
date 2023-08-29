def eh_vogal(caractere):
    vogais = 'AEIOUaeiou'
    return caractere in vogais

nome_arquivo = input('Digite o nome do arquivo texto: ')

try:
    with open(nome_arquivo, 'r', encoding='UTF-8') as arquivo:
        conteudo = arquivo.read()
        contador_vogais = 0
        for caractere in conteudo:
            if eh_vogal(caractere):
                contador_vogais += 1
        print(f'O arquivo contém: {contador_vogais} vogais')
except FileNotFoundError:
    print(f'O arquivo {nome_arquivo} não foi encontrado')
except Exception as e:
    print('Ocorreu um erro:', e)
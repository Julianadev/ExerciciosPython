def eh_vogal(caractere):
    vogais = 'AEIOUaeiou'
    return caractere in vogais

def eh_consoante(caractere):
    consoantes = 'BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz'
    return caractere in consoantes

nome_arquivo = input('Digite o nome do arquivo: ')


try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        contador_vogais = 0
        contador_consoantes = 0
        for caractere in conteudo:
            if eh_vogal(caractere):
                contador_vogais += 1
            elif eh_consoante(caractere):
                contador_consoantes += 1
        print(f'Total de vogais: {contador_vogais}')
        print(f'Total de consoantes: {contador_consoantes}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except Exception as e:
    print('Ocorreu um erro: ', e)

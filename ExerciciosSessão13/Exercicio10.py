def cidade_mais_populosa(cidades, habitantes):
    indice_max = habitantes.index(max(habitantes))
    return cidades[indice_max]

print('Digite o nome da cidade e o número de habitantes ou então "sair" para sair')

nome_arquivo = input('Digite um nome para o arquivo: ')
nome_arquivo_saida = input('Digite o nome do outro arquivo: ')

cidades = []
habitantes = []

with open(nome_arquivo, 'a', encoding='UTF-8') as arquivo:
    while True:
        cidade = input('Digite o nome da cidade: ').capitalize()
        if cidade.lower() == 'sair':
            break
        habitante = int(input('Digite o número de habitantes: '))
        if habitante <= 0:
            print('Número de habitantes inválido')
            continue
        cidades.append(cidade)
        habitantes.append(habitante)
        arquivo.write(f'{cidade} - {habitante}\n')

print('Registros adicionados com sucesso!')

cidade_mais_populosa = cidade_mais_populosa(cidades, habitantes)

with open(nome_arquivo_saida, 'w', encoding='UTF-8') as arquivo:
    arquivo.write(f'Cidade mais populosa: {cidade_mais_populosa}')

with open(nome_arquivo_saida, 'r') as arquivo:
    print(arquivo.read())


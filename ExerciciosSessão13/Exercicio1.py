with open('arq.txt', 'w', encoding='UTF-8') as arquivo:
    try:
        while True:
            conteudo = input('Digite o conteúdo do arquivo ou então digite 0 para sair: ')
            if conteudo != '0':
                arquivo.write(conteudo)
                arquivo.write('\n')
            else:
                print('Encerrando o programa...')
                break
    except Exception as e:
        print('Ocorreu um erro:', e)

with open('arq.txt', 'r') as arquivo:
    lendo_conteudo = input('Deseja visualizar o arquivo? S/N ')
    if lendo_conteudo.upper() == 'S':
        print(arquivo.read())
    else:
        print('Encerrando o programa...')
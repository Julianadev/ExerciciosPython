
def exponenciacao(X, Z):
    return X ** Z

X = float(input('Digite o número: '))
Z = int(input('Digite a potência: '))

print(f'{X} elevado a {Z} = {exponenciacao(X, Z)}')
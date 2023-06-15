
a = int(input("Digite o número a: "))
h = int(input("Digite o número h: "))


vetor_a = []
while a > 0:
    digito = a % 10
    vetor_a.append(digito)
    a //= 10

vetor_h = []
while h > 0:
    digito = h % 10
    vetor_h.append(digito)
    h //= 10


tamanho_maximo = max(len(vetor_a), len(vetor_h))
vetor_soma = []
carry = 0  # Variável para controlar o "vai um"
for i in range(tamanho_maximo):
    digito_a = vetor_a[i] if i < len(vetor_a) else 0
    digito_h = vetor_h[i] if i < len(vetor_h) else 0

    soma = digito_a + digito_h + carry
    digito_soma = soma % 10
    carry = soma // 10

    vetor_soma.append(digito_soma)


if carry > 0:
    vetor_soma.append(carry)

print("Vetor de soma:", vetor_soma)




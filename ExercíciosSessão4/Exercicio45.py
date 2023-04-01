"""
Faça um programa para converter uma letra
maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema.
"""

letra = input("Digite uma letra maiúscula: ")
letra_minuscula = chr(ord(letra) + 32)
print(f"A letra minúscula correspondente é: {letra_minuscula}")
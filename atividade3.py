print("========================================")
print("ANALISADOR DE NOME")
print("========================================")

nome = input("Digite seu nome completo: ")

quantidade = len(nome)
primeira_letra = nome[0]
ultima_letra = nome[-1]
maiusculo = nome.upper()

print("========================================")
print("RESULTADOS DA ANÁLISE:")
print("========================================")

print(f"Nome digitado: {nome}")
print(f"Quantidade de caracteres: {quantidade}")
print(f"Primeira letra: {primeira_letra}")
print(f"Última letra: {ultima_letra}")
print(f"Nome em maiúsculas: {maiusculo}")

print("========================================")
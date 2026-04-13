print("========================================")
print("CALCULADORA DE DOBRO E METADE")
print("========================================")

numero = int(input("Digite um número inteiro: "))

dobro = numero * 2
metade = numero / 2

print("========================================")
print("RESULTADOS:")
print("========================================")

print(f"Número digitado: {numero}")
print(f"Dobro: {dobro}")

if metade.is_integer():
    metade = int(metade)

print(f"Metade: {metade}")

print("========================================")
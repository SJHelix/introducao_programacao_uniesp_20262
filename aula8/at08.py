numeros = []

for i in range(1, 11):
    n = int(input(f"Digite o {i}° número: "))
    numeros.append(n)

busca = int(input("Digite um número para buscar: "))

resultados = 0

for n in numeros:
    if n == busca:
        resultados += 1

print(f"O número {busca} aparece {resultados} vezes.")

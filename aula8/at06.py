numeros = []

for i in range(1, 8):
    n = int(input(f"Digite o {i}° número: "))
    numeros.append(n)

numeros_invertidos = []

for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])

print(f"Lista original: {numeros}")
print(f"Lista invertida: {numeros_invertidos}")

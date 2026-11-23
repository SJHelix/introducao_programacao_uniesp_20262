numeros = []

for i in range(1, 11):
    n = int(input(f"Digite o {i}° número: "))
    numeros.append(n)

soma_pares = 0
soma_impares = 0

for n in numeros:
    if n % 2 == 0:
        soma_pares += n
    else:
        soma_impares += n

print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")

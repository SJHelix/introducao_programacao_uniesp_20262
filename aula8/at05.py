numeros = []
repetidos = []

for i in range(1, 9):
    n = int(input(f"Digite o {i}° número: "))

    if n in numeros:
        repetidos.append(n)
    numeros.append(n)

if len(repetidos) > 0:
    print("Existem números repetidos.")
else:
    print("Não existem números repetidos.")
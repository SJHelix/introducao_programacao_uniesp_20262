numeros = []

for i in range(1, 9):
    n = int(input(f"Digite o {i}° número: "))
    numeros.append(n)

maiores10 = []

for n in numeros:
    if n > 10:
        maiores10.append(n)

print(f"Lista original: {numeros}")
print(f"Números maiores que 10: {maiores10}")

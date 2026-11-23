numeros = []
pares = []
impares =[]

for i in range(1,11):
  num = int(input(f"Digite o {i}° número: "))
  numeros.append(num)

for n in numeros:
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)

print(f"Lista original: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
positivos = []
negativos = []
zeros = []

for i in range(1,11):
  n = int(input(f"Digite o {i}° número: "))
  if n > 0:
    positivos.append(n)
  elif n < 0:
    negativos.append(n)
  else:
    zeros.append(n)

print(f"Quantidade de positivos: {len(positivos)}")
print(f"Quantidade de negativos: {len(negativos)}")
print(f"Quantidade de zeros: {len(zeros)}")
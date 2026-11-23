numeros = []
posicao = maior = 0

for i in range(0,8):
  num = int(input(f"Digite o {i+1}° número: "))
  if i == 0:
    maior = num
    position = i
  numeros.append(num)

for i in range(0, len(numeros)):
  if numeros[i] > maior:
    maior = numeros[i]
    posicao = i

print(f"Maior número: {maior}")
print(f"Posição: {posicao}")
notas = []
acima_media = []
soma_notas = 0

for i in range(1,7):
  n = float(input(f"Digite a {i}° nota: "))
  notas.append(n)

for nota in notas:
  soma_notas += nota
  if nota >= 7.0:
    acima_media.append(nota)

media = soma_notas / len(notas)

print(f"Média da turma: {media:.1f}")
print(f"Notas acima da média: {acima_media}")
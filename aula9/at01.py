matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)

diagonal = []
for i in range(3):
    for j in range(3):
        if i == j:
            diagonal.append(matriz[i][j])

print(f"Diagonal: {diagonal}")
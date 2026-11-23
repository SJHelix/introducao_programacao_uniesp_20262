nomes = []
notas = []

for i in range(1, 6):
    nome = input(f"Digite o nome do {i}° aluno: ")
    nota = float(input("Digite a nota desse aluno: "))

    nomes.append(nome)
    notas.append(nota)

for i in range(0, len(nomes)):
    if notas[i] >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"Aluno: {nomes[i]}")
    print(f"Nota: {notas[i]}")
    print(f"Situação: {situacao}")
    print(f"-"*20)

num = int(input("Digite um número para contar pares: "))
pares = 0

for i in range(1, num+1):
    if i % 2 == 0:
        pares += 1

print(f"Existem {pares} pares até esse número.")
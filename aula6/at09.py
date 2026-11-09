contp = contn = contz = 0

for i in range(1,11):
    n = int(input("Digite um número: "))
    if n > 0:
        contp += 1
    elif n < 0:
        contn += 1
    else:
        contz += 1

print(f"Positivos: {contp}")
print(f"Negativos: {contn}")
print(f"Zeros: {contz}")
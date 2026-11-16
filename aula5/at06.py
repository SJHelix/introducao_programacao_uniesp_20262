soma = 0
n = 1

while n <= 5:
    user_num = int(input(f"Digite o {n}o número: "))
    soma += user_num
    n += 1

print(f"A soma entre os números é igual a {soma}")
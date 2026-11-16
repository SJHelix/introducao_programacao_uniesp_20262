total = 0
n = 1

while n <= 5:
    user_num = int(input(f"Digite o {n}o número: "))
    total += user_num
    n += 1

media = total / 5
print(media)
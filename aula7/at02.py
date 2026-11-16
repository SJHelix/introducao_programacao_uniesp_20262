num = [1,5, 3, 7, 2, 8, 6]
maior = num[0]

for i in range(len(num)):
    if num[i] > maior:
        maior = num[i]

print(maior)
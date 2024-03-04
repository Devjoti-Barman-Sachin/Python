count_positive_value = 0
for index in range(0, 6):
    inpt = float(input())
    if inpt > 0:
        count_positive_value += 1
print(f'{count_positive_value} valores positivos')
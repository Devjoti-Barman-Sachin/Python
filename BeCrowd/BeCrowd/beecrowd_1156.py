sum = 0
lst = []
for i in range(1, 40, 2):
    lst.append(i)
for i in range(0, len(lst)):
    sum = sum + (lst[i])/(2**i)
print(f'{sum:.2f}')

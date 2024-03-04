i = 0
lst = []
while i != 10:
    x = int(input())
    if x <= 0:
        y = 1
        lst.append(y)
    else:
        lst.append(x)
    i += 1
for i in range(0, len(lst)):
    print(f'X[{i}] = {lst[i]}')

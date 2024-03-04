lst = []
for i in range(0, 100):
    x = float(input())
    lst.append(x)
    if lst[i] <= 10:
        print(f'A[{i}] = {lst[i]:.1f}')

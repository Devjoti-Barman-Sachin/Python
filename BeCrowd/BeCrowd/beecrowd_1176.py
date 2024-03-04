x = 0
lst = []
for i in range(0, 2):
    lst.append(i)
x = lst[0] + lst[1]
lst.append(x)
n = int(input())
for i in range(2, n+1):
    x = lst[i-1] + lst[i]
    lst.append(x)
for i in range(0, n):
    x = int(input())
    print(f'Fib({x}) = {lst[x]}')
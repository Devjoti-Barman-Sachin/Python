lst = list(map(int, input().split()))
a = lst[0]
n = 0
sum = 0
for i in range(1, len(lst)):
    n = lst[i]
    if n > 0:
        break
for i in range(n):
    sum = sum + i + a
print(sum)
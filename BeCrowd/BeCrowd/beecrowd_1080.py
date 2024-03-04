max = 0
counter = 0
for i in range(1, 101):
    x = int(input())
    if max < x:
        max = x
        counter = i

print(max)
print(counter)
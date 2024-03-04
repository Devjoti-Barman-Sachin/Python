x = int(input())
y = int(input())
sum = 0
if x > y:
    for i in range(x-1, y, -1):
        if i % 2 == 1:
            sum = sum+i
else :
    for i in range(y-1, x, -1):
        if i % 2 == 1:
            sum = sum+i
print(sum)

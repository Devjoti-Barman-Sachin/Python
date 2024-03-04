x = int(input())
for i in range(0, x):
    y, z = map(int, input().split())
    sum = 0
    counter = 0
    s = y+(2*z)
    for i in range(y, s):
        if i % 2 == 1:
            sum += i
    print(sum)

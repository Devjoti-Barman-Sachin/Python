n = int(input())
for index in range(0, n):
    sum  = 0
    x, y = map(int, input().split())
    if x > y:
        for check in range(x-1, y, -1):
            if check%2 == 1:
                sum = sum + check
        print(sum)
    else:
        for check in range(y-1, x, -1):
            if check%2 == 1:
                sum = sum + check
        print(sum)
flag = 0
while True:
    x= int(input())
    if x == 0:
        flag = 1
    else:
        value = []
        for i in range(1, x+1):
            value.append(i)
        print(*value[:])
    if flag == 1:
        break
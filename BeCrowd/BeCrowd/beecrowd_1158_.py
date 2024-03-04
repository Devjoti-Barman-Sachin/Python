x = int(input())
for i in range(0, x):
    y, z = map(int, input().split())
    sum = 0
    counter = 0
    while True:
        if counter == z:
            print(sum)
            break
        else:
            if y%2 == 0:
                y += 1
            elif y % 2 == 1:
                counter += 1
                sum += y
                y += 1
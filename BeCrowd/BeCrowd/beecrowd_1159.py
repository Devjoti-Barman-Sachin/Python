while True:
    x = int(input())
    sum = 0
    counter = 0
    s = x+10
    if x == 0:
        break
    for i in range(x, s):
        if i % 2 == 0:
            sum += i
            counter += 1
    print(sum)
            
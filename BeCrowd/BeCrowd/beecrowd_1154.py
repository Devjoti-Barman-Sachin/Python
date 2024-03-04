c = 0
sum = 0
avg = 0
while True:
    n = int(input())
    if n > 0:
        c += 1
        sum =  sum + n
        pass
    elif n < 0:
        avg = sum / c
        print(f'{avg:.2f}')
        break
    
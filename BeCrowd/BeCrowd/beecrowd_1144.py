n = int(input())
for i in range(1, n+1):
    for f in range(i, i+1):
        mult1 = i*i
        sum1 = mult1+1
        mult2 = mult1*i
        sum2 = mult2+1
        print(f'{i} {mult1} {mult2}')
        print(f'{i} {sum1} {sum2}')


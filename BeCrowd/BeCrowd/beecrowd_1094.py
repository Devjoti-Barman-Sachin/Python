n = int(input())
sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
for index in range(0, n):
    x, y = input().split()
    x = int(x)
    if y == 'C':
        sum1 = sum1+x
    elif y == 'R':
        sum2 = sum2+x
    elif y == 'S':
        sum3 = sum3+x
sum = sum1 + sum2 + sum3
percentage_of_c = (sum1/sum)*100.00
percentage_of_r = (sum2/sum)*100.00
percentage_of_s = (sum3/sum)*100.00
print(f'Total: {sum} cobaias')
print(f'Total de coelhos: {sum1}')
print(f'Total de ratos: {sum2}')
print(f'Total de sapos: {sum3}')
print(f'Percentual de coelhos: {percentage_of_c:.2f} %')
print(f'Percentual de ratos: {percentage_of_r:.2f} %')
print(f'Percentual de sapos: {percentage_of_s:.2f} %')

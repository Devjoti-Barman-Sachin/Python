x = int(input())
y = int(input())
c = 1
current_sum = x
while y <= x:
    y = int(input())
while current_sum <= y:
    x += 1
    current_sum += x
    c += 1
print(c)
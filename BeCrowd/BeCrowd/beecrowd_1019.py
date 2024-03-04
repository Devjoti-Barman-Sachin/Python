x = int(input())
a = x//3600
y = x%3600
b = y//60
z = y % 60
print(f'{a}:{b}:{z}')

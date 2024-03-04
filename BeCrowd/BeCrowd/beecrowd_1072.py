n = int(input('How many integers you want to read: '))
in_count = 0
out_count = 0
for index in range(0, n):
    x = int(input('Enter value: '))
    if x >= 10 and x <= 20:
        in_count += 1
    else:
        out_count += 1
print(f'{in_count} in')
print(f'{out_count} out')
    
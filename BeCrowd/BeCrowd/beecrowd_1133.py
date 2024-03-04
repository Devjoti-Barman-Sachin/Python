x = int(input())
y = int(input())
value = []
if x>y:
    for i in range(y+1, x):
        if i % 5 == 2 or i % 5 == 3:
            value.append(i)
else:
    for i in range(x+1, y):
        if i % 5 == 2 or i % 5 == 3:
            value.append(i)

for i in range(0, len(value)):
    print(value[i])

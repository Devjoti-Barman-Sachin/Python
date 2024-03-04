store = 0
n = int(input())
for i in range(1, n+1):
    value = ''
    if i == 1:
        for j in range(i, i+3):
            value = value + str(j)+' '
            store = j
        print(''.join(value),'PUM')
    elif i > 1:
        s = store+2
        for j in range(s, s+3):
            store = j
            value = value + str(j)+' '
        print(''.join(value),'PUM')


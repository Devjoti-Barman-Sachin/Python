n = int(input())
for index in range(0, n):
    x, y = map(int, input().split())
    try:
        result = x / y
        print(f'{result:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')

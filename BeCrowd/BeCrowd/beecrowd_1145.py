x, y = map(int, input().split())
if x < y:
    value = []
    for i in range(1, y+1):
       value.append(i)
    
    for j in range(0, len(value), x):
            print(*value[j:j+x])
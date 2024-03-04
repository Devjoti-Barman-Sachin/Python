
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
p1 = (x2-x1)*(x2-x1)
p2 = (y2-y1)*(y2-y1)
distance = (p1+p2)**0.5
print(f'{distance:.4f}')

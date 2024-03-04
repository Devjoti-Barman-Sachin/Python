n, m = map(int, input().split())
s = set()

for _ in range(m):
    x = int(input())
    s.add(x)

print(n - len(s))

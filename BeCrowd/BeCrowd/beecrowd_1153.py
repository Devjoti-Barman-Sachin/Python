n = int(input())
fact = n
for i in range(1, n):
    fact = fact * (n-i)
print(fact)
i = 1
lst = []
x = int(input())
store = x
lst.append(x)
while i != 10:
    make_double = store + store
    store = make_double
    lst.append(make_double)
    i += 1
for i in range(0, len(lst)):
    print(f'N[{i}] = {lst[i]}')

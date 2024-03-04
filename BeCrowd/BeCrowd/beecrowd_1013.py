a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
x = abs(a-b)
y = abs(b-c)
major_ab = int((a+b+x)/2)
major_bc = int((b+c+y)/2)
if(major_ab>major_bc):
    print(f'{major_ab} eh o maior')
else:
    print(f'{major_bc} eh o maior')


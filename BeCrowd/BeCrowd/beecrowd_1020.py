x = int(input())
a = x//365
b = x%365
c = b//30
d = b%30
print(f'{a} ano(s)')
print(f'{c} mes(es)')
print(f'{d} dia(s)')

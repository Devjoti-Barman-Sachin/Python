a, b, c = map(float, input().split())
if(a+b > c) and (b+c > a) and (a+c > b):  	
    perimetro = a+b+c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((a+b)/2)*c
    print(f'Area = {area:.1f}')
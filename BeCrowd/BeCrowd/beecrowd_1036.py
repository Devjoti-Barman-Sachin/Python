import math
def baskharas_formula(a,b,c):
    if a<=0:
        print('Impossivel calcular')
    else:
        x = (b**2)-(4*a*c)
        if x>=0:
            r1 = (-b+math.sqrt((x)))/(2*a)
            r2 = (-b-(math.sqrt(x)))/(2*a)
            print(f'R1 = {r1:.5f}')
            print(f'R2 = {r2:.5f}')
        else:
             print('Impossivel calcular')
a,b,c = map(float, input().split())
baskharas_formula(a,b,c)


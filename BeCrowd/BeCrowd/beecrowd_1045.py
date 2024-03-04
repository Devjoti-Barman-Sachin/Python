numbers = input().split()
numbers = [float(number) for number in numbers]
numbers.sort(reverse=True)
a = numbers[0]
b = numbers[1]
c = numbers[2]
if a >= b+c:
    print('NAO FORMA TRIANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')   
elif (a**2) == (b**2) + (c**2):
    print('TRIANGULO RETANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == complex or a == c:
        print('TRIANGULO ISOSCELES')  
elif (a**2) > (b**2) +(c**2 ):
    print('TRIANGULO OBTUSANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')  
elif (a**2) < (b**2) +(c**2 ):
    print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')



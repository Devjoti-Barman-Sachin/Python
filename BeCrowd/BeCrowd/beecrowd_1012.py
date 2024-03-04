a, b, c = input().split()
pi = 3.14159
a = float(a)
b = float(b)
c = float(c)
tri = (1/2)*a*c
cir = c*c*pi
trap = (1/2)*(a+b)*c
sqr = b*b
rec = (a*b)
print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {sqr:.3f}')
print(f'RETANGULO: {rec:.3f}')

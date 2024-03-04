a = float(input())
print('NOTAS:')
print(f'{int(a//100)} nota(s) de R$ 100.00')
a = a%100
print(f'{int(a//50)} nota(s) de R$ 50.00')
a = a%50
print(f'{int(a//20)} nota(s) de R$ 20.00')
a = a%20
print(f'{int(a//10)} nota(s) de R$ 10.00')
a = a%10
print(f'{int(a//5)} nota(s) de R$ 5.00')
a = a%5
print(f'{int(a//2)} nota(s) de R$ 2.00')
a = a%2
print('MOEDAS:')
print(f'{int(a//1)} moeda(s) de R$ 1.00')
a = a%1.00
print(f'{int(a//0.50)} moeda(s) de R$ 0.50')
a = a%0.50
print(f'{int(a//0.25)} moeda(s) de R$ 0.25')
a = a%0.25
print(f'{int(a//0.10)} moeda(s) de R$ 0.10')
a = a%0.10
print(f'{int(a//0.05)} moeda(s) de R$ 0.05')
a = a%0.05
print(f'{int(a//0.01)} moeda(s) de R$ 0.01')

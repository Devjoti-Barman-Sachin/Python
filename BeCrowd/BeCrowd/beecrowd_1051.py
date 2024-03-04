salary = float(input())
if salary >= 0.0 and salary <= 2000.00:
    print('Isento')
elif salary >= 2000.01 and salary <= 3000.00:
    rest_salary = salary - 2000 
    taxes = (rest_salary*0.08)
    print(f'R$ {taxes:.2f}')
elif salary >= 3000.01 and salary <= 4500.00:
    rest_salary = salary - 3000
    taxes = (1000*0.08) + (rest_salary * 0.18)
    print(f'R$ {taxes:.2f}')
else:
    rest_salary = salary - 4500
    taxes = (1000*0.08) + (1500*0.18) + (rest_salary * 0.28)
    print(f'R$ {taxes:.2f}')

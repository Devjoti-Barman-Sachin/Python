salary = float(input())
if salary >= 0 and salary <= 400.00:
    percentage = salary*.15
    total_salary = salary + percentage
    print(f'Novo salario: {total_salary:.2f}')
    print(f'Reajuste ganho: {percentage:.2f}')
    print(f'Em percentual: 15 %')
elif salary >= 400.01 and salary <= 800.00:
    percentage = salary*.12
    total_salary = salary + percentage
    print(f'Novo salario: {total_salary:.2f}')
    print(f'Reajuste ganho: {percentage:.2f}')
    print(f'Em percentual: 12 %')
elif salary >= 800.01 and salary <= 1200.00:
    percentage = salary*.10
    total_salary = salary + percentage
    print(f'Novo salario: {total_salary:.2f}')
    print(f'Reajuste ganho: {percentage:.2f}')
    print(f'Em percentual: 10 %')
elif salary >= 1200.01 and salary <= 2000.00:
    percentage = salary*.07
    total_salary = salary + percentage
    print(f'Novo salario: {total_salary:.2f}')
    print(f'Reajuste ganho: {percentage:.2f}')
    print(f'Em percentual: 7 %')
else:
    percentage = salary*.04
    total_salary = salary + percentage
    print(f'Novo salario: {total_salary:.2f}')
    print(f'Reajuste ganho: {percentage:.2f}')
    print(f'Em percentual: 4 %')
    
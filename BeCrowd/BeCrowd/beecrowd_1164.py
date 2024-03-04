test_cases = int(input())
for i in range(test_cases):
    testing_value = int(input())
    sum = 0
    for i in range(1, testing_value):
        if testing_value % i == 0:
            sum = sum + i
    if sum == testing_value:
        print(f'{testing_value} eh perfeito')
    else:
        print(f'{testing_value} nao eh perfeito')
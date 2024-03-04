test_cases = int(input())
for i in range(test_cases):
    testing_value = int(input())
    counter = 0
    for i in range(1, testing_value+1):
        if testing_value % i == 0:
            counter += 1
        else:
            counter += 0
    if counter == 2:
        print(f'{testing_value} eh primo')
    else:
        print(f'{testing_value} nao eh primo')
    
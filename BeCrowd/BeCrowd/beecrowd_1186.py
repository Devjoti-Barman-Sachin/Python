def matrix_input():
    x = input()
    lst = []
    sum = 0
    avg = 0
    i = 0
    counter = 0
    while i != 144:
        y = float(input())
        lst.append(y)
        i += 1

    new_sublists = len(lst)//12
    nested_lists = [lst[i * 12: (i + 1) * 12] for i in range(new_sublists)] #deviding the list into 12 sublists that makes an array [12][12]
    print(nested_lists[:])

    for i in range(0, len(nested_lists)):  # iteration row wise
        for j in range(len(nested_lists)-i,len(nested_lists)):   # iteration row wise
            sum += nested_lists[i][j]  
            counter += 1

    avg = sum / counter
    if x == 's' or x == 'S':
        print(f'{sum:.1f}')
        
    elif x == 'm' or x == 'M':
        print(f'{avg:.1f}')

matrix_input()
def matrix_input(n):
    x = input()
    lst = []
    sum = 0
    avg = 0
    i = 0
    while i != 144:
        y = float(input())
        lst.append(y)
        i += 1

    new_sublists = len(lst)//12
    nested_lists = [lst[i * 12: (i + 1) * 12] for i in range(new_sublists)] ## deviding the list into 12 sublists
    print(nested_lists[:])

    lst_for_sum = []
    for i in range(0, len(nested_lists)):
        lst_for_sum.append(nested_lists[i][n]) #added column in another list
    print(lst_for_sum[:])
    for i in range(0, len(lst_for_sum)):
        sum += lst_for_sum[i]
    avg = sum /12

    if x == 's' or x == 'S':
        print(f'{sum:.1f}')
    elif x == 'm' or x == 'M':
        print(f'{avg:.1f}')

n = int(input())
matrix_input(n)
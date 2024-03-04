while True:
    flag = 0
    x = input()
    x = int(x)
    if x > 0:
        def matrix_print(n):
            for i in range(1, n + 1):
                row = []
                for j in range(1, n + 1):
                    cell_value = min(i, j, n - i + 1, n - j + 1)
                    row.append(f"{cell_value: >3}") 
                print(" ".join(row))
            print()
        
    elif x == 0:
        flag = 1
    if flag == 1:
        break
    matrix_print(x)
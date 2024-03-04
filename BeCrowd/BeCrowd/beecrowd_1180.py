def lowest(n):
    updated_list = list(map(int, input().split()))
    lowest_number = updated_list[0]
    index = 0
    for i in range(0, len(updated_list)):
        if lowest_number > updated_list[i]:
            index = i
            lowest_number = updated_list[i]
    print(f'Menor valor: {lowest_number}')
    print(f'Posicao: {index}')
  
n = int(input())
lowest(n)
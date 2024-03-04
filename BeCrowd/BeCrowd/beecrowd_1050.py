code_number_list = [61, 71, 11, 21, 32, 19, 27, 31]
desination_list = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
x = int(input())
found = len(code_number_list)
for index in range(0, len(code_number_list)):
    if x == code_number_list[index]:
        print(desination_list[index])
        break
    else:
        found = found-1
if found == 0:
    print('DDD nao cadastrado')

    
    
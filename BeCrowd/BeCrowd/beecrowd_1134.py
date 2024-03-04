alcohol_c = 0
gasoline_c = 0
diesel_c = 0
counter = 0
while True:
    x = int(input())
    if x > 0:
        if x == 1:
            alcohol_c += 1
        elif x == 2:
            gasoline_c += 1
        elif x == 3:
            diesel_c += 1
        elif x == 4:
            counter += 1
        else:
            pass
    if counter == 1:
        print('MUITO OBRIGADO')
        print(f'Alcool: {alcohol_c}')
        print(f'Gasolina: {gasoline_c}')
        print(f'Diesel: {diesel_c}')
        break
    
        
    
    
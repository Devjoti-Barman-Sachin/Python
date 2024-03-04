counter = 0
sum = 0
flag = 0
while True:
    n = float(input())
    if n <= 0 or n > 10.0:
        print('nota invalida')
    else:
        sum = sum+n
        counter = counter + 1
        if counter == 2:
            media = sum / 2
            print(f'media = {media:.2f}')
            print('novo calculo (1-sim 2-nao)')
            while True:
                z = int(input())
                if z == 1:
                    counter = 0
                    sum = 0
                    break
                elif z < 1 or z > 2:
                    print('novo calculo (1-sim 2-nao)')
                elif z == 2:
                    flag = 1
                    break
            
            if flag == 1:
                break
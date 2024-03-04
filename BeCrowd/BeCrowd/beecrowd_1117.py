counter = 0
sum = 0
while True:
    n = float(input())
    if n <= 0 or n >= 11.0:
        print('nota invalida')
    else:
        sum = sum+n
        counter = counter + 1
        if counter == 2:
            media = sum / 2
            print(f'media = {media:.2f}')
            break

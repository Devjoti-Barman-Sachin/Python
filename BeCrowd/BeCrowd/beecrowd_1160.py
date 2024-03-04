x = int(input())
for i in range(0, x):
    pa, pb, g1, g2 = map(float, input().split(' ')) 
    year = 0
    while pa <= pb and year <= 100:
        pa = int(pa) + (int(pa*(g1/100)))
        pb = int(pb) + (int(pb*(g2/100)))
        year += 1
    if year > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{year} anos.')

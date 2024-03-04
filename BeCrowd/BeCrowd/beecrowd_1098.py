i = 0

for index in range(int(i), 11):
    j = 1
    for sequence in range(int(j), int(j)+3, 1):
            l = i
            k = sequence+l
            if (l > 0 and l < 1) or ( l >= 1.1 and l <= 1.8) :
               print(f'I={l:.1f} J={k:.1f}')
            else:
                print(f'I={l:.0f} J={k:.0f}')   
    j = j+0.2
    i = i+0.2

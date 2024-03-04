inter_counter = 0
germio_counter = 0
draw_counter = 0
match_counter = 0
flag = 0
while True:
    x, y = map(int, input().split())
    if x > y:
        inter_counter += 1
        match_counter += 1
        print('Novo grenal (1-sim 2-nao)')
        while True:
                z = int(input())
                if z == 1:
                    break
                elif z == 2:
                    flag = 1
                    break
    elif x < y:
        germio_counter += 1
        match_counter += 1
        print('Novo grenal (1-sim 2-nao)')
        while True:
            z = int(input())
            if z == 1:
                break
            elif z == 2:
                flag = 1
                break
    else:
        draw_counter += 1
        match_counter += 1
        print('Novo grenal (1-sim 2-nao)')
        while True:
            z = int(input())
            if z == 1:
                break
            elif z == 2:
                flag = 1
                break
    if flag == 1:
        print(f'{match_counter} grenais')
        print(f'Inter:{inter_counter}')
        print(f'Gremio:{germio_counter}')
        print(f'Empates:{draw_counter}')
        if inter_counter > germio_counter:
            print('Inter venceu mais')
        else:
            print('Gremio venceu mais')    
        break

    

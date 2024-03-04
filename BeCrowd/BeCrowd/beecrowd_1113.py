while True:
    try:
        x, y = map(int, input().split())
        if x == y:
            break
        else:
            if x > y:
                print('Decrescente')
            else:
                print('Crescente')
    except ValueError:
        break
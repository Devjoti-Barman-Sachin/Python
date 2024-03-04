x = 24
a, b = map(int, input().split())
if a > b:
    gamming_time = (x - a) + b
    print(f'O JOGO DUROU {gamming_time} HORA(S)')
elif a < b:
    gamming_time = b - a
    print(f'O JOGO DUROU {gamming_time} HORA(S)')
else:
    print(f'O JOGO DUROU {x} HORA(S)')



a, b, c, d = map(int, input().split())
game_start_time_hour_to_second = a*3600
game_start_time_minute_to_second = b*60
game_start_time_second = game_start_time_hour_to_second + game_start_time_minute_to_second
game_end_time_hour_to_second = c*3600
game_end_time_minute_to_second = d*60
game_end_time_second = game_end_time_hour_to_second + game_end_time_minute_to_second
if game_end_time_second>  game_start_time_second:
    time_difference = game_end_time_second - game_start_time_second
    game_in_hour = time_difference // 3600
    game_in_second = time_difference % 3600
    game_in_second = game_in_second // 60
    print(f'O JOGO DUROU {game_in_hour} HORA(S) E {game_in_second} MINUTO(S)')
elif game_end_time_second < game_start_time_second:
    time_difference = (24*3600) - game_start_time_second
    game_in_hour = time_difference // 3600
    game_in_second = time_difference % 3600
    game_in_second = (game_in_second+game_end_time_minute_to_second) // 60
    print(f'O JOGO DUROU {game_in_hour + c} HORA(S) E {game_in_second} MINUTO(S)')
else :
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
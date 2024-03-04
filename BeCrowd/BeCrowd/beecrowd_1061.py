date1 = input().split()
dia = date1[1]
dia = int(dia)
x1,y1,z1=map(int,input().split(":"))
date2 = input().split()
dia2 = date2[1]
dia2 = int(dia2)
x2,y2,z2=map(int,input().split(":"))
day = (dia2-dia)
hour = x2-x1
minute = y2-y1
second = z2-z1

if second > 59:
    minute += 1   
    second -= 1
elif second < 0:
    second = 60+second
    minute -= 1

if minute > 59:
    hour += 1
    minute -= 1
elif minute < 0:
    minute = 60+minute
    hour -= 1

if hour > 23:
    day += 1
    hour -= 1
elif hour < 0:
    hour = 24+hour
    day -= 1


print(f'{day} dia(s)')
print(f'{hour} hora(s)')
print(f'{minute} minuto(s)')
print(f'{second} segundo(s)')

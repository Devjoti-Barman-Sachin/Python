n = int(input())
for inpt in range(0, n):
    x = int(input())
    if x % 2 == 0:
        if x == 0:
            print("NULL")
        elif x < 0:
            print("EVEN NEGATIVE")
        else:
            print("EVEN POSITIVE")
    else:
        if x == 0:
            print("NULL")
        elif x < 0:
            print("ODD NEGATIVE")
        else:
            print("ODD POSITIVE")
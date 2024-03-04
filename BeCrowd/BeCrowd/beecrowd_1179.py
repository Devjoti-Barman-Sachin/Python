even = []
odd = []
j = 0
while j != 15:
    x = int(input())
    if x % 2 == 0 :
        even.append(x)
        if len(even) == 5:
            for i in range(0, len(even)):
               print(f'par[{i}] = {even[i]}')
            even.clear()
    else:
        odd.append(x)
        if len(odd) == 5:
            for i in range(0, len(odd)):
                print(f'impar[{i}] = {odd[i]}')
            odd.clear()
    j += 1

if len(odd) != 0:
    for i in range(0, len(odd)):
        print(f'impar[{i}] = {odd[i]}')
if len(even) != 0:
    for i in range(0, len(even)):
        print(f'par[{i}] = {even[i]}')




      
            
    

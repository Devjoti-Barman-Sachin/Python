lst = []
for i in range(0, 20):
    x = int(input())
    lst.append(x)

updated_list = []  # updating the list from last to fast

k = (len(lst))-1
for i in range(0, k+1):    #updating the list
        y = lst[k-i]
        updated_list.append(y)

for i in range(0, len(updated_list)):
     print(f'N[{i}] = {updated_list[i]}')

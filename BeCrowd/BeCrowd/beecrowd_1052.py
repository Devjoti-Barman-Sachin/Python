month_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
x = int(input())
for index in range(0, 13):
    if x == month_number_list[index]:
        print(month_list[index])
        break
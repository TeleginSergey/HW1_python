#входные данные
n = int(input())
#если число оканчивается на цифры 5, 6, 7, 8, 9 или это числа 11-19 то окончание ов
if (n%10 >= 5 or n%10 == 0) or (n>10 and n<20):
    print(n,'korov')
#если число оканчивается на числа 2, 3, 4, то окончание овы
elif n%10 > 1:
    print(n,'korovy')
#если число оканчивается на число 1, то окончание ова
else:
    print(n,'korova')

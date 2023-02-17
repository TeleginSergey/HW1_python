a = int(input())
b = int(input())
c = int(input())
#дискриминант
discr = b**2 - 4*a*c
#обязательно чтобы дискриминант был неотрицательным
if discr >= 0:
    #корни
    d = (-b+ (discr)**0,5)/2/a
    e = (-b- (discr)**0,5)/2/a
    #корни могут быть одинаковыми
    if d == e:
        print(d)
    else:
        print(e, d)
import random

a = int(input("размер теругольника - "))
for i in range(1, a+1):
    if i == 1:
        print(' '*(a-1)+'*')
    elif i == a:
        print('*'*(2*a-1))
    else:
        b = ' ' * (a - i)
        b = ' '*(2*i-3)
        print(b+'*'+b + '*')

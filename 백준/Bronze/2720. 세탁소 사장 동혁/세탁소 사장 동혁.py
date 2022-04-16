from decimal import Decimal
T = int(input())

cng =[25,10,5,1]
for _ in range(T):
    C = int(input())

    for i in range(len(cng)):
        num = C // cng[i]
        print(num, end=' ')
        # print('C',C)
        C -= num * cng[i]
        # print(num * cng[i])
        # print('num',num)
        # print('cng[i]',cng[i])
        # print('C',C)

    print()

n  = int(input())
res = 0
def findCreator(n):
    for i in range(n): #198
        sum = 0
        for j in str(i):
            sum+=int(j)
        if(i+sum)==n:
            print(i)
            return
    print(0)
    return 

findCreator(n)
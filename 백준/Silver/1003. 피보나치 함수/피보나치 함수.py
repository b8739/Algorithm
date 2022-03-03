t = int(input())
memo = [0]*41
dictt={}
zero = 0 
one = 0

def f(n):
    global zero
    global one
    if n==0:
        zero+=1
        return 1
    if n==1:
        one+=1
        return 1
    if memo[n]:
        zero+=dictt[str(n)][0]
        one+=dictt[str(n)][1]
        return memo[n]
    else:
        memo[n] = f(n-1)+f(n-2)
        dictt[str(n)] = [zero,one]
        return memo[n]
    
for _ in range(t):
    zero,one = 0 ,0
    f(int(input()))
    print(zero,one,sep=' ')
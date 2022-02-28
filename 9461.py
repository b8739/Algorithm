memo = [0] * 101

def nasun(x):
    if memo[x]!=0: 
        return memo[x]
    if 0<=x<=3: 
        return 1
    if 4<=x<=5: 
        return 2
    if 6<=x: 
        memo[x] = nasun(x-5) + nasun(x-1) 
        return  memo[x]
    
n = int(input())

for _ in range(n):
    v = int(input())
    print(nasun(v))


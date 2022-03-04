import math

n = int(input())
dp = [0,0,1,1,2,3,2]
for i in range(7,n+1):
    a,b,c = math.inf,math.inf,dp[i-1]
    if i%3==0:
        a = dp[i//3]
    if i%2==0:
        b = dp[i//2]
    dp.append(min(a,b,dp[i-1])+1)
print(dp[n])
    
    


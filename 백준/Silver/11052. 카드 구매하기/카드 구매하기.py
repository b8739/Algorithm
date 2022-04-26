
n = int(input())

s = [0] + list(map(int,input().split()))
dp = [0]+ [0 for _ in range(n+1)]


def sol(dp):
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i] = max(dp[i],dp[i-j] + s[j])
    print(dp[n])

sol(dp)        

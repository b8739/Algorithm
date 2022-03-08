n = int(input())
dp = [0,1,3]
for i in range(3,n+1):
    v=dp[i-1]+(2*dp[i-2])
    dp.append(v)
print(dp[n]%10007)



n = int(input())

dp = [0,1,2,3,5,8]

if n<5:
    print(dp[n])
else:
    for i in range(6,n+1):
        dp.append((dp[i-1]+dp[i-2])%15746)

    print(dp[n])
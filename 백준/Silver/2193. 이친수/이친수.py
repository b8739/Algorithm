n = int(input())

dp = [0,1,1,2]

if n<4:
    print(dp[n])
else:
    for i in range(4,n+1):
        dp.append(dp[i-2]+dp[i-1])

    print(dp[n])
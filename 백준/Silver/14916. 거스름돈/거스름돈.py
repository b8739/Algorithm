n = int(input())
dp = [0,-1,1,-1, 2 ,1]

if n < 6:
    print(dp[n])

else:
    for i in range(6,n+1):
        if i < 10:
            dp.append(dp[i-2]+1)
        else:
            dp.append(dp[i-5]+1)


    print(dp[n])

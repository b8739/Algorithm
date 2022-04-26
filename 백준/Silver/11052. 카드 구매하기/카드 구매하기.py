n = int(input())

s = [0] + list(map(int,input().split()))

dp = [0]

dp.append(s[1])

def sol(dp):
    if n > 1:
        dp.append(max(dp[1] * 2, s[2]))    
    if n < 2:
        print(dp[n])
        return
    

    for i in range(3,n+1):
        maxv = s[i]

        for j in range(1,i):
            if i % j == 0:
                maxv = max(maxv,dp[j] * i//j)
            else:
                maxv = max(maxv,dp[j] + dp[i-j])

        dp.append(maxv)
    print(dp[n])

sol(dp)       
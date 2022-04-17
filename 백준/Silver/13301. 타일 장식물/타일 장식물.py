n = int(input())

dp = [0,1,1]

def get_perimeter(n):
    global dp
    for i in range(2,n+1):
        dp.append(dp[i]+dp[i-1])
    perimeter = (dp[n]+dp[n+1])*2
    return perimeter

print(get_perimeter(n))
n = int(input())
s  = list(map(int,input().split()))
dp = [0] * n

def maxPrefixSum():
    global dp
    if n==1:
        print(s[0])
        return
    else:
        dp[0] = s[0]
        dp[1] = max(s[1],s[0]+s[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1]+s[i],s[i])
        print(max(dp))
maxPrefixSum()
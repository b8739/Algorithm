N = int(input())
S  = list(map(int,input().split()))
dp = [0] * N

def maxPrefixSum():
    global dp
    dp[0] = S[0]
    for i in range(1,N):
        dp[i] = max(dp[i-1]+S[i],S[i])
    print(max(dp))
maxPrefixSum()
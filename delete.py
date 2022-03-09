n = int(input())
s = [0]

for _ in range(n):
    s.append(int(input()))

dp = [0]*(n+1)
dp[1],dp[2] = s[1],s[1]+s[2]

for i in range(3,n+1):
     dp[i] = max(s[i-1]+s[i],dp[i-2]+s[i])

print(dp[n])
# 6

# 10
# 20
# 15
# 25
# 10
# 20
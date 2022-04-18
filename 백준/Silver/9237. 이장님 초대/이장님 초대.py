N = int(input())
S = list(map(int,input().split()))
S.sort(reverse=True)
result = 0
for i in range(N):
    result = max(result,S[i]+i)
print(result+2)

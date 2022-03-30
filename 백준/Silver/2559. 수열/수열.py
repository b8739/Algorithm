N, K = map(int,input().split())

S = list(map(int,input().split()))

sumValue = 0

for i in range(K):
    sumValue+=S[i]

maxv=sumValue

for i in range(K,N):
    sumValue+=S[i]
    sumValue-=S[i-K]
    maxv = max(maxv, sumValue)

print(maxv)
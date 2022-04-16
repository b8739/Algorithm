N, L = map(int,input().split())
S = list(map(int,input().split()))
S.sort()

for i in range(N):
    if L >= S[i]:
        L+=1
print(L)
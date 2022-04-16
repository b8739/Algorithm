N,K = map(int, input().split())

S = list(input()) #HPHPHPHPHP

res = 0

for i in range(N):
    if S[i]=='P':

        for j in range(max(i-K,0),min(i+K+1,N)):
            if S[j] == 'H':
                S[j] = 0
                res+=1
                break
print(res)

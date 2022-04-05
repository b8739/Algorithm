N, L  = map(int,input().split())

S = list(map(int,input().split()))

S.sort()

count = 1

start = S[0]-1
end = start+L

for i in range(1,N):
    if S[i]<=end:
        continue
    else:
        count+=1
        start = S[i]-1
        end = start+L
        
print(count)


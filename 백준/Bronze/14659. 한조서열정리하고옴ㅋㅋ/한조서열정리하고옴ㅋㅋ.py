N = int(input())
S = list(map(int,input().split()))

result = 0
idx1= 0

while True:
    if idx1 >= N-1:
        break

    idx2 = idx1+1
    cnt = 0

    while idx2 <= N-1:
        
        if S[idx1] > S[idx2]:
            cnt+=1
            idx2+=1
            continue
        else:
            idx1 = idx2
            break

    result = max(result,cnt)

    if idx2 >= N-1:
        idx1=idx2

print(result)
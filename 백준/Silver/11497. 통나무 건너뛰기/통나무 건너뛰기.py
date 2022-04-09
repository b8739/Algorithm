T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    S.sort()
    maxv=0
    for i in range(N-2):
        maxv = max(maxv,abs(S[i]-S[i+2]))
    print(maxv)
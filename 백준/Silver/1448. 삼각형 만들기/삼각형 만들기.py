import sys
input = sys.stdin.readline
N = int(input())
S = [int(input())  for _ in range(N)]
S.sort(reverse=True)
res = -1
for i in range(N-2):
    if S[i+1]+S[i+2]>S[i]:
        res = S[i]+S[i+1]+S[i+2]
        break
print(res)
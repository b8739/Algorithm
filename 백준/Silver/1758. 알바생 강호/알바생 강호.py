N = int(input())
S = [int(input()) for _ in range(N)]
S.sort(reverse=True)
result = 0
for idx,v in enumerate(S):
    tip = v-idx
    if tip>0:
        result+=v-idx
print(result)
# 15650번
n,m = list(map(int,input().split()))
s = []

def dfs(x):
#     print(f'{x}st dfs')
    if len(s)==m:
#         print(f'{x}여기로 Return')
        print(' '.join(map(str,s)))
        return
    for i in range(x,n+1):
#         print(f'{i}st loop')
        if i not in s:
#             print('i:',i)
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)
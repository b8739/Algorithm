import sys

sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for i in range(n+1)]
roots = [-1]*(n+1)
visited = [False]* (n+1)
for i in range(1,n):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)   

def dfs(x):
    visited[x]=True
    if not tree[x]:
        return
    else:
        for i in tree[x]:
            if not visited[i]:
                visited[i]=True
                dfs(i)
                roots[i] = x
        return
dfs(1)
for i in roots[2:]:
    print(i)

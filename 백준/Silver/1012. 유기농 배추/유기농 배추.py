import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x>=m or y>=n or x<=-1 or y<=-1:
        return False
    if graph[x][y]==1:
        graph[x][y] = 0
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False

t = int(input())

for _ in range(t):
    m,n,k = map(int,input().split())

    graph = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1

    cnt = 0

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                cnt+=1
    print(cnt)
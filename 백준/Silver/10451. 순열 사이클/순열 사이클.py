import sys
sys.setrecursionlimit(100000)

t = int(input())

def dfs(x):
    global visited
    visited[x] = True
        #아직 방문하지 않았을 때만 방문하고, 방문하면 방문처리
    if not visited[graph[x]]:
        dfs(graph[x])

for i in range(t):
    #초기화
    n = int(input())
    graph = list(map(int,input().split()))
    graph.insert(0,0)

    visited = [False] * (n+1)
    
    cnt = 0
    
    for k in range(1,n+1):
        if not visited[k]:  # 0
            dfs(k)
            cnt+=1
    print(cnt)

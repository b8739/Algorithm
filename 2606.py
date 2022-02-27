#2606번 바이러스

n = int(input())
cn = int(input())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(i)
            
        
for _ in range(cn):
    a,b = map(int,input().split())
    graph[a].append(b) #[[],[2,5],[3]...]
    graph[b].append(a)

dfs(1)
print(cnt)
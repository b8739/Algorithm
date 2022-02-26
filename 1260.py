from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
            
def dfs(key): 
    if visited[key] == False: 
        visited[key] = True
        
        print(key, end=' ')
        
        for i in graph[key]:
            dfs(i) 


def bfs(key): 
    visited[key] = True
    queue = deque([key])
    while queue:
        val = queue.popleft()
        print(val, end=' ')
        
        for i in graph[val]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


#sorting
for i in range(1,n+1):
    graph[i].sort()
    

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)
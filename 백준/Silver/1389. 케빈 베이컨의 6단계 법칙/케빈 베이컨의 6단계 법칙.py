from collections import deque
n, m = map(int,input().split())
# n,m = 5,5
distance = [0]*(n+1)
# graph = [[],[3,4],[3],[1,2],[1,3,5],[4]]
graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(start):
    visited = [start]
    distance = [0]*(n+1)
    queue=deque()
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                distance[i] += distance[v]+1
                visited.append(i)
                queue.append(i)
    return sum(distance)
final = []

for i in range(1,n+1):
    # 초기화
    # 케빈 합 계산
    final.append(BFS(i))
    
print(final.index(min(final))+1)
      
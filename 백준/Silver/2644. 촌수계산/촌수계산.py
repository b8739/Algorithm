from collections import deque
# n = 9
n = int(input())
# A,B = 7,3
A,B = map(int,input().split())
# m = 7
m = int(input())
graph = [[]for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


# graph = [[],[2,3],[1,7,8,9],[1],[5,6],[4],[4],[2],[2],[2]]

visited = [0]*(n+1)

queue = deque()
queue.append(A)

flag = False

while queue:
    v = queue.popleft()
    for j in graph[v]:
        
        if visited[j] == 0:
            visited[j] = visited[v]+1
            queue.append(j)

print(visited[B] if visited[B]>0 else -1)

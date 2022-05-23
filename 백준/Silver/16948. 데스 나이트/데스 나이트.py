from collections import deque

N = int(input())
r1,c1,r2,c2 = map(int,input().split())

visited = [[0 for _ in range(N)]for _ in range(N)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        a,b = queue.popleft()
        
        if a == r2 and b == c2: return visited[a][b]
        
        for i in range(6):
            nx = a+dx[i]
            ny = b+dy[i]
            if -1<nx<N and -1<ny<N and not visited[nx][ny]:
                visited[nx][ny] = visited[a][b]+1
                queue.append((nx,ny))
result = bfs(r1,c1)  
  
if result == None:
    result=-1

print(result)
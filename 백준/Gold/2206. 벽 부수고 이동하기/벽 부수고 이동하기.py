from collections import deque


n,m = map(int,input().split())
s = [list(map(int,input())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

#parameter: x,y,wall
def bfs():
    q = deque()
    q.append((0,0,0))
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0]=1
    while q:
        x,y,wall = q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][wall]
        #조건
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if -1<nx<n and -1<ny<m:
                if s[nx][ny] == 0 and visited[nx][ny][wall]==0:
                    visited[nx][ny][wall] = visited[x][y][wall]+1
                    q.append((nx,ny,wall))    
                elif s[nx][ny] == 1 and wall==0:
                    visited[nx][ny][wall+1] = visited[x][y][wall]+1
                    q.append((nx,ny,wall+1))  
    return -1

print(bfs())
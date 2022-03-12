from collections import deque

N = int(input())
S = []
max_num = 0

#최고값 찾기
for i in range(N):
    S.append(list(map(int,input().split())))
    for j in range(N):
        max_num = max(S[i][j],max_num)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b,rain,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if -1<nx<N and -1<ny<N:
                if S[nx][ny]>rain and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
result = 0

for i in range(max_num):
    visited = [[0] * N for i in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if S[j][k] > i and visited[j][k] == 0: 
                bfs(j,k,i,visited)
                cnt+=1
    result = max(result,cnt)
print(result)


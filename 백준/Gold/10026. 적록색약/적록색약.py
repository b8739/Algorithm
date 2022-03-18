# dfs이나
# r랑 b를 동일시하는 경우와
# 분리해서 생각하는 경우로 나뉘어진다
#if문
import sys
sys.setrecursionlimit(10000)

# N = 5
# S = [['R','R','R','B','B'],['G','G','B','B','B'],['B','B','B','R','R'],['B','B','R','R','R'],['R','R','R','R','R']]
N = int(input())
S = [list(map(str,input())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)] 


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    visited[x][y] = True

    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]

        if -1<nx<N and -1<ny<N:
            #일반
            if S[nx][ny] == S[x][y] and not visited[nx][ny] :
                dfs(nx,ny)
            #적록색약
            # if S[x][y] in ['R','G'] and S[nx][ny] in ['R','G'] and not visited2[nx][ny]:
            #     visited2[nx][ny] = True
            #     dfs(nx,ny)
            #     cnt_2+=1
# visited[0][0] = True
# visited2[0][0] = True

cnt = 0


    # visited = [[False] * N] * N 
#색약 아닐때
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            a = dfs(i,j)
            cnt+=1

print(cnt,end= " ")

#색약 일때
visited = [[False for _ in range(N)] for _ in range(N)] 

cnt = 0

for i in range(N):
    for j in range(N):
        if S[i][j]=='R':
            S[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            cnt+=1
print(cnt)


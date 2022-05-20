n = int(input())

s = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<n and s[nx][ny]==1:
            s[nx][ny] = 0
            cnt+=1
            cnt += dfs(nx,ny)
    return cnt 

result = []

for i in range(n):
    for j in range(n):
        if (s[i][j]==1): 
            result.append(dfs(i,j))

result.sort()    

print(len(result))

for r in result:
    if r ==0: print(1)
    else: print(r)
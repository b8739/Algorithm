import sys
sys.setrecursionlimit(100000)
R,C = map(int,input().split())

yard = [list(input()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

total_v = 0
total_o = 0

o = 0
v = 0

def dfs(x,y):
    global v,o
    # 개수 세기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1<nx<R and -1<ny<C and yard[nx][ny]!='#':
            if yard[nx][ny] == 'v':
                v+=1
            elif yard[nx][ny] == 'o':
                o+=1
            yard[nx][ny]='#' #방문처리
            dfs(nx,ny)
    return 
            
for x in range(R):
    for y in range(C):
        if yard[x][y] != '#':
            if yard[x][y] == 'v':
                v+=1
            elif yard[x][y] == 'o':
                o+=1

            yard[x][y] = '#'
            
            dfs(x,y)
            
            if o>v:
                total_o+=o
            else:
                total_v+=v

            o = 0
            v = 0

print(total_o,total_v)
    
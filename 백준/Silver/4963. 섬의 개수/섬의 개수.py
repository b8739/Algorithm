#1의 개수
#연결되어 있으면 하나로 친다
#True가 될때마다 +1되는것
#연결할때마다0으로 바꾸면 됨
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

import sys
sys.setrecursionlimit(10000)  # 재귀 제한을 확대해야 함.

def dfs(x,y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i] 
        if nx<h and ny<w and nx>-1 and ny>-1 and mp[nx][ny]==1:
            mp[nx][ny]=0
            dfs(nx,ny)
        
  
while True:
    w,h = map(int,input().split())

    if w ==0 and h==0:
        break

    mp = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if mp[i][j] != 0: #바다면 거름
                dfs(i,j) #실행된것만으로 일단 섬 확보
                cnt+=1
    print(cnt)

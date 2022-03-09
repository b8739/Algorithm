# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
#  보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다 (상하좌우)
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
# 2 ≤ M,N ≤ 1,000
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# 모두 익은 상황: 최소날짜
# 모두 익지 못하는 상황 (반복문 끝): -1
# 시작부터 모두 익은 상황 (반복문 끝): 0


from collections import deque

m,n = map(int,input().split())

queue = deque([])

dx = [0,0,-1,+1]
dy = [-1,+1,0,0]

res = 0

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():  
    while queue:
        x,y = queue.popleft() #초기에 넣은 값
        for i in range(4):
            nx,ny = x+ dx[i],y+ dy[i]
            if -1< nx < n and -1< ny < m and graph[nx][ny] == 0:
                graph[nx][ny] += graph[x][y]+1 
                queue.append([nx,ny]) #0,1,0,1,
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
            
bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
    
print(res - 1)
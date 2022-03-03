import copy

# n,m = 7,7
# nm = [[2, 0, 0, 0, 1, 1, 0],
#  [0, 0, 1, 0, 1, 2, 0],
#  [0, 1, 1, 0, 1, 0, 0],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0, 0]]
n,m = map(int,input().split())
nm = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

virus_p = []
max_safe = 0

#바이러스 위치 기록
for i in range(n):
    for j in range(m):
        if nm[i][j] == 2:
            virus_p.append([i,j])


def make_wall(start,cnt):
    global max_safe
    
    #끝나는 조건
    if cnt == 3:
        fake_nm = copy.deepcopy(nm)
        for p in virus_p:
            infect(fake_nm,p[0],p[1])
        #안전구역 (0) 세기
        safe_counts = sum(i.count(0) for i in fake_nm)
        max_safe = max(max_safe,safe_counts)
        return
    #재귀 조건
    for i in range(start,n*m):
        x = i//m
        y = i%m
        if nm[x][y] == 0:
            nm[x][y] = 1
            make_wall(i,cnt+1)
            nm[x][y] = 0
  
#됨

def infect(fake_nm,a,b): 
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        if nx >=0 and ny>=0 and nx <n and ny<m:
            if fake_nm[nx][ny] ==0:
                fake_nm[nx][ny]=2
                infect(fake_nm,nx,ny)
                    
#안됨 (IndexError: list index out of range)
# def infect(fake_nm,a,b): 
#     if a <0 and b<0 and a>=n and b>=m:
#         return False
#     for i in range(4):
#         nx = a+dx[i]
#         ny = b+dy[i]
#         if fake_nm[nx][ny] ==0:
#             fake_nm[nx][ny]=2
#             infect(fake_nm,nx,ny)

make_wall(0,0)
print(max_safe)

"""
틀렸던 이유
- 방향 벡터를 key값으로 주는게 아니라 '기존 좌표+벡터'로 했어야 함
- dfs(infect)의 함수 상단에 끝나는 조건을 설정하려고 했는데 그렇게 못함. 
왜냐하면 해당 위치가 0인지 검증해야 하는데(fake_nm[nx][ny]) 만약 방향벡터가 범위 밖이면 배열에 접근했을때 
IndexError: list index out of range 에러가 뜸

애초에 감염은 2만 할 수 있고, 그럴려면
방향 벡터로 움직이려는 곳이 범위 내인지 먼저 확인하고, 그게 0이면 재귀를 해야함.
"""
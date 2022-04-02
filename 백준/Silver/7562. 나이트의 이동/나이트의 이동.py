"""
알고리즘: BFS
최소 이동횟수를 구하는 것이기 때문에 DFS보다는 BFS를 사용
이동할때마다, B 배열에 (방문처리 기능도 함) 그 이전 value값을 다음 index value값에 넣기
"""
from collections import deque
#나이트의 이동방식
dx = [2,1,-1,-2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

T = int(input())

def BFS(i,j):
    # 시작점과 종점이 같으면 바로 return
    if i == x2 and j ==y2:
        print(0)
        return

    queue = deque()
    queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if -1<nx<size and -1<ny<size and B[nx][ny]==0:
                queue.append([nx,ny])
                B[nx][ny] = B[x][y]+1
                #끝나는 조건
                if nx == x2 and ny == y2:
                    print(B[nx][ny])
                    return

for i in range(T):
    # 데이터 받기
    size = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    # 보드 만들기
    B = [[0 for _ in range(size)] for _ in range(size)]

    BFS(x1,y1)


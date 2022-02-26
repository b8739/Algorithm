#단지번호붙이기

n = int(input())
graph = []

cnt = 0
count = []
def dfs(x,y):
    global cnt
    if x>=n or y>=n or x<=-1 or y<=-1:
        return False
    #1일때만 방문등록
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt+=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for _ in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            count.append(cnt)
            cnt = 0
print(len(count))
count.sort()
for c in count:
    print(c)
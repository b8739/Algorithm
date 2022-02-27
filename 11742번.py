#11742 연결 요소의 개수
import sys

sys.setrecursionlimit(10000)  # 재귀 제한을 확대해야 함.

def dfs(x):
    if not visited[x]:
        visited[x] = True
        for i in graph[x]:     
                dfs(i)           
        return True
    return False #방문했었으면 return False

#True가 될 때마다 1을 더한다
n,m = map(int,input().split()) # [[],[2,3],[1,4]]

visited = [False] * (n + 1)

graph = [[] for _ in range(n+1)] #0 포함해서 생성

for i in range(m):
    a,b = map(int,sys.stdin.readline().split()) # 1,2
    graph[a].append(b)
    graph[b].append(a)
    
sum = 0

for i in range(1, n+1):
        if dfs(i) == True:
            sum+=1
print(sum)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
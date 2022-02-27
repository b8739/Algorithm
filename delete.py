import sys

def dfs(x):
    if x >= n: 
        return False
    
    if visited[x]==False:
        visited[x] = True
        for i in graph[x]:     
                dfs(i)           
        return True
    return False

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
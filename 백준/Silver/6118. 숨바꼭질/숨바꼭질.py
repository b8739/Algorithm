from collections import deque 
N,M = map(int,input().split())

S = [[] for _ in range(N+1)] 
dist = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    S[a].append(b)
    S[b].append(a)


def bfs():
    global dist
    node = 1
    dist[node]=1
    frontier = [node]
    while frontier:
        next_frontier = []
        for i in frontier:
            for j in S[i]: 
                if dist[j] ==0:
                    dist[j] = dist[i]+1
                    next_frontier.append(j)   
        frontier = next_frontier
    return
    
bfs()

maxv = max(dist)

print(dist.index(maxv),maxv-1,dist.count(maxv))

from collections import deque

n,k = map(int,input().split())

def bfs():  #5
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v==k: 
            print(dist[v])
            break
        for nx in [v-1,v+1,v*2]: #4,6,10
            if 0 <= nx <= Max and not dist[nx]:
                dist[nx] = dist[v]+1
                queue.append(nx)


Max = 10 **5 

dist = [0]* (Max+1)
bfs()

from collections import deque

N = int(input())

relationship= [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    s = list(input())
    for j in range(N):
        if s[j] == 'Y':
            relationship[i][j] = 1

def bfs(i):
    global friends
    visited  = [0] * N
    visited[i] = True
    q = deque([(i,0)])
    count = 0

    while q:
        j,cnt = q.popleft()
        if cnt>=2:
            break

        for k in range(N):
            if not visited[k] and relationship[j][k]:
                count += 1
                visited[k] = True
                q.append((k,cnt+1))
            
    return count

result = 0
for i in range(N):
    result = max(result,bfs(i))
print(result)
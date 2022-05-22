# bfs를 사용해서 거리를 기록
# 1부터 시작해서 마지막번호까지를
# 그럼 마지막번호가 1번째 답
# 2번째답은 거리
# 3번째는 같은 헛간 개수


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
    queue = deque()
    queue.append(1)
    dist[1]=1

    while queue:
        node = queue.popleft()
        for n in S[node]:
            if dist[n] ==0:
                dist[n] = dist[node]+1
                queue.append(n)
    # for i in range(1,M):
    #     for j in S[i]:
    #         if dist[j] ==0:
    #             dist[j] = dist[i]+1

    return
bfs()

maxv = max(dist)

print(dist.index(maxv),maxv-1,dist.count(maxv))


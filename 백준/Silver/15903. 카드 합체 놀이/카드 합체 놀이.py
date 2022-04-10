import heapq
N,M = map(int,input().split())
S = list(map(int,input().split()))

heapq.heapify(S)

for i in range(M):
    v1 = heapq.heappop(S)
    v2 = heapq.heappop(S)
    for i in range(2):
        heapq.heappush(S,v1+v2)
print(sum(S))
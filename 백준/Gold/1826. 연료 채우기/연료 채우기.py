import heapq

n = int(input())
gs = []
#최소힙
for _ in range(n):
    dist,f = map(int,input().split())
    heapq.heappush(gs,[dist,f])
#최대힙
target,fuel = map(int,input().split())

filled = []
cnt = 0

while target>fuel:
   
    while gs and gs[0][0]<=fuel:
        dist, f = heapq.heappop(gs)
        heapq.heappush(filled,-1*f)
   
    if not filled:
        cnt = -1
        break
   
    f = heapq.heappop(filled)
    fuel += -1*f
    cnt+=1

print(cnt)
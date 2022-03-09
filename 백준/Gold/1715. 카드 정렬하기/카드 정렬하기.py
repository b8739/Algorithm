#heapify, heapq, heappop, heappush

import heapq

n= int(input())
cardlist = [int(input()) for _ in range(n) ]
heapq.heapify(cardlist)
res = 0

while len(cardlist)!=1:
    a = heapq.heappop(cardlist)
    b = heapq.heappop(cardlist)
    res += a+b
    heapq.heappush(cardlist,a+b)
print(res)
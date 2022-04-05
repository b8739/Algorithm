import heapq
import sys

input = sys.stdin.readline
N = int(input())

arr = []
cnt = 0

for _ in range(N):
    v = int(input())
    if v == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)*(-1))
    else:
        heapq.heappush(arr,-(v))

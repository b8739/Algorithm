import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr,int(input()))
for i in range(n):
    print(heapq.heappop(arr))

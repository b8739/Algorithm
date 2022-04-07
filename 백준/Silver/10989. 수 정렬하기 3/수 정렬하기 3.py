import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*10001

for _ in range(n):
    v = int(input())
    arr[v]+=1

for i,v in enumerate(arr):
    for j in range(v):
        print(i)
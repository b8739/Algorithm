import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    
    asset = []
    profit = 0

    maxv = s[-1]

    for j in range(n-2,-1,-1):
        if s[j] > maxv:
            maxv = s[j]
        else:
            profit += maxv-s[j] 

    print(profit)
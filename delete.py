import sys

input = sys.stdin.readline

n,t = map(int,input().split())
res = 0

parents = [i for i in range(n)]

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

# def union(a,b):
#     a = find(a)
#     b = find(b)
#     if a!=b:
#         parents[max(a,b)] = min(a,b)
#         return False
#     else:
#         return True
def union(x, y, idx):
    global res
    x = find(x)
    y = find(y)
    if x != y:
        parents[max(x,y)] = min(x,y)
    elif res == 0:
        res = idx


for idx in range(t):
    a,b = map(int,input().split())
    union(a,b,idx)
    
print(res)
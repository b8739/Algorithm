def find(x):
    if parents[x] == x:
        return x
    else: 
        parents[x] = find(parents[x])
        return parents[x] 

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parents[b]=a
        number[a]+=number[b]

n = int(input())
for _ in range(n):
    f = int(input())
    parents = {}
    number = {}
    for _ in range(f):

        a,b=map(str,input().split())
        if a not in parents:
            parents[a]=a
            number[a]=1
        if b not in parents:
            parents[b]=b
            number[b]=1
        union(a,b)
        print(number[find(a)])
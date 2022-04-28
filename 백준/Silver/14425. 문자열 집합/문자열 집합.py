n,m = map(int,input().split())

a = {}

for i in range(n):
    a[input()]=True

cnt = 0    

for i in range(m):
    m = input()
    if m in a.keys():
        cnt+=1
print(cnt)
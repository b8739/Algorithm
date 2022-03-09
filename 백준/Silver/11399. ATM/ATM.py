n = int(input())
p = list(map(int,input().split()))

p.sort()

last = p.pop()

sum = 0

idx = len(p)+1

for pp in p: # 1 2 3 3 
    sum+=pp*idx
    idx-=1
    
print(sum+last)
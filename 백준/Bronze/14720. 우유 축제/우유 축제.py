N = int(input())
S = list(map(int,input().split()))
P = [0,1,2]

count = 0

for i in S:
    if i == count % 3:
        count+=1
print(count)

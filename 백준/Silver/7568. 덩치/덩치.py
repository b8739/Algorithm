n = int(input())
people = [list(map(int,input().split())) for _ in range(n)]

for idx,i in enumerate(people):
    cnt = 0 
    for j in people:
        if i[0]<j[0] and i[1]<j[1]:
            cnt+=1
    print(cnt+1)
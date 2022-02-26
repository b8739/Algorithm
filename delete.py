import sys

input = sys.stdin.readline

T = int(input())

# s = list()

for i in range(T):
    n = int(input())
    s = [0]*n
    #n만큼 성적을 받는 과정
    for j in range(n):
        a,b = map(int,input().split())
        # s.append([a,b])
        s[j] = [a,b]
    cnt=1
    
    s.sort()
    
    man = s[0][1]
    
    for j in s[1:]:
        if man>j[1]:
            cnt+=1
            man=j[1]
            
    print(cnt)
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int,input().split()))
total = sum(s)

if total % 3 != 0 :
    print('NO')
else:
    cnt = 0
    days = total // 3 
    
    for i in range(n):
        cnt+=s[i] // 2
        
    if cnt>=days:
        print('YES')
    else:
        print('NO')
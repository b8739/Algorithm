#1002번 터렛
import math
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)
    #if랑 elif 순서 바뀌면 안되는데 왜 인지 알아볼것
    if d==0 and r1==r2:
        print(-1)   
    elif abs(r2-r1)==d or r1+r2==d :
        print(1)

    elif r2+r1<d or abs(r2-r1)>d:
         print(0)
        
    elif abs(r2-r1) < d < (r1 + r2):
        print(2)
   # else:
    #    print(0)
        
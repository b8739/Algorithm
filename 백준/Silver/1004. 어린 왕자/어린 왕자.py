T = int(input())
for i in range(T):
    count = 0   
    # 출발지와 도착지
    x1,y1,x2,y2 = map(int,input().split())
    # 행성계의 개수
    N = int(input())
    # 중점 좌표와 반지름
    for j in range(N):
        cx,cy,r = map(int,input().split())
        dist_1 = (x1 - cx)**2 + (y1-cy)**2
        dist_2 = (x2 - cx)**2 + (y2-cy)**2
        r_squared = r**2
        if dist_1<r**2 and dist_2<r**2:
            continue
        elif r_squared > dist_1 or r_squared > dist_2:
            count +=1

    print(count)

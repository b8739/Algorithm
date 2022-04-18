N,M = map(int,input().split())
rect = [list(map(int,input())) for _ in range(N)]

max_dist = 0
max_result = 1

for i in range(N-1):
    for j in range(M):
        V = rect[i][j]
        max_dist = 0
        for k in range(j+1,M):
            #정사각형 범위를 벗어나면 break
            dist = abs(j - k)
            if  dist > N:
                break
            #가장 멀리 떨어져있는 점을 구하기 위해서 max_dist 갱신
            if V == rect[i][k]:
                max_dist = max(max_dist, dist)
                #가장 큰 정사각형의 넓이를 구하기 위해서 max_result 갱신
                if i+max_dist<N and V == rect[i+max_dist][j] and V == rect[i+max_dist][k]:
                    size = (max_dist+1)*(max_dist+1)
                    max_result = max(max_result,size)

print(max_result)
        

# 1931번 회의
 
""" 성공 """
# 17번째 줄의 lambda에서 두번째 index는 고려 안 함

n = int(input())
time = [[0]*2 for _ in range(n)]

cnt = 1

for i in range(n):
    s,e= map(int,input().split())
    time[i][0] = s
    time[i][1] = e   


time.sort(key = lambda x: (x[1],x[0]))

end = time[0][1]

for i in time[1:]:
    if end <= i[0]:
        end = i[1]
        cnt+=1
print(cnt)    

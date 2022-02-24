#끝나는 시간은 무조건 시작 시간보다 크므로, 끝나는 시간이 낮은거 기준으로 해야함
#시작 시간이 같다면, 끝나는 시간이 낮은게 좋음

"""두번째 실패"""
n = int(input())
time = [[0]*2 for _ in range(n)]

cnt = 1

for i in range(n):
    s,e= map(int,input().split())
    time[i][0] = s
    time[i][1] = e   
#time = [[s,e],[s,e],[s,e],[s,e]]

time.sort(key = lambda x: (x[1], x[0]))

end = time[0][1]

for i in time[1:]:
    if end <= i[0]:
        end = i[1]
        cnt+=1
print(cnt)    
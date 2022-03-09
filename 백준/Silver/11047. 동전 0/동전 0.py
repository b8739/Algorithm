from bisect import bisect_left,bisect_right

n,k = map(int,input().split())

m = []
cnt = 0

for _ in range(n):
    m.append(int(input()))
    
idx = bisect_right(m,k) #7
#bisect left는 <=이기 때문에 찾는 값과 동일한 값이 있으면 그 index를 반환, 없으면 가장 근접한 값의 다음 인덱스를 반환

m = m [0: idx]

for i in m[::-1]:
    if k%i==0:
        cnt+=k//i
        break
    else:
        cnt += k//i
        k %= i

print(cnt)  
    

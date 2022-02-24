# 11047 동전 0
#내가 짠 코드
from bisect import bisect_left,bisect_right

n,k = map(int,input().split())

m = []
cnt = 0

for _ in range(n):
    m.append(int(input()))

idx = bisect_right(m,k) #7
#bisect left는 <=이기 때문에 찾는 값과 동일한 값이 있으면 그 index를 반환, 없으면 가장 근접한 값의 다음 인덱스를 반환하기 때문에 bisect_right을 사용

m = m [0: idx]

for i in m[::-1]:
    if k%i==0:
        cnt+=k//i
        break
    else:
        cnt += k//i
        k %= i

print(cnt)  
    
"""
풀이

bisect를 안 써도 됐는데 복습 겸 사용해서 풀어봤다.
문제를 보면 1<=N<=10으로 N이 주어지기 때문에 bisect를 사용하기 않고 그냥 역순으로 해도 된다.

"""

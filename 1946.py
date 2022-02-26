"""시간 초과 O"""
import sys

input = sys.stdin.readline

t = int(input())

s = list()

for i in range(t):
    n = int(input())
    cnt=1
    for j in range(n):
        a,b = map(int,input().split())
        s.append([a,b])
    
    s.sort()
    
    max = s[0][1]
    
    for j in s[1:]:
        if max>i[1]:
            cnt+=1
            max=i[1]

    print(cnt)

"""시간 초과 X"""
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    s = [0]*n
    for j in range(n):
        a,b = map(int,input().split())
        s[j] = [a,b]
    cnt=1
    
    s.sort()
    
    man = s[0][1]
    
    for j in s[1:]:
        if man>j[1]:
            cnt+=1
            man=j[1]
            
    print(cnt)

"""
시간 초과 났던 요인
처음에는 sys.stdin.readline을 안 써서 인줄 알았는데 써도 시간초과 남
append하는 것보다 n 사이즈로 배열을 만들어두고 (s = [0]*n) index로 값 넣으니까 시간 초과가 안남

검색해보니

"앞의 코드에서는 append() 함수를 이용해서 빈 리스트에 입력받은 값을 저장해줬다.
하지만 이 경우 리스트를 먼저 초기화해주고 인덱스를 이용해서 접근해서 값을 저장하면 속도가 조금 더 개선된다."

라고 한다.
"""
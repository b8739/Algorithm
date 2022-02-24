# 1931번 회의
 
"""첫번째 실패 """
# dict는 키가 똑같은 쌍이 있을 수가 없는데 이 사실을 간과함
n = int(input())
c = {}
cnt = 1

for _ in range(n):
    s,e= input().split()
    c[s] = int(e)
    
sorted_dict = sorted(c.items(), key = lambda item: item[1])

t = sorted_dict[0][1]

for i in sorted_dict[1:]:
    if t <= int(i[0]):
        print(i)
        t = i[1]
        cnt+=1
print(cnt)    


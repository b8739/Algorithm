# 문제: 네 번째 점

a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

x_group = [a,c,e]
y_group = [b,d,f]

x = 0
y = 0

for i in x_group:
    if x_group.count(i) == 1:
        x = i
        
for j in y_group:
    if y_group.count(j) == 1:
        y = j
        
print(f'{x} {y}')    
 
# 풀이 방법 
# x좌표, y좌표 값이 각각 두번씩 나온다는 것을 활용


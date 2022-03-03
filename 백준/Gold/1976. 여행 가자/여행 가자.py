n = int(input()) #200이하의 값
m = int(input()) #1000이하

parents = [i for i in range(n)] #0부터 n까지 자기 자신을 갖게 됨 

#배열로 받고
#배열을 순회하면서 1이면 그 좌표의 x와 y도시를 union해준다.
#일단 부모로 자기 자신을 갖고 있다.
#union을 해주면 자기보다 작은 값을 갖게 된다.
#여행이 가능하려면 중복하더라도 서로 연결되어있어야 한다. 작은 수를 부모로 주기 때문에 숫자가 다 같으면 여행 가능하다
def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        return y
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a>b:
        parents[a] = b
    if a<b:
        parents[b] = a
    pass

union_status = [list(map(int,input().split())) for _ in range(n)]

plan = map(int,input().split())
final= []

for i in range(n):
    for j in range(n):
        if union_status[i][j] == 1:
            union(i,j)
            
for i in plan:
    final.append(find(i-1))
    
if len(set(final)) == 1:
    print("YES")
else: print("NO")
n, m = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
#같은 수를 여러번 골라도 된다. == 순서가 상관없다.
temp = []
def solve():
    global temp
    
    if len(temp) == m:
        print(*temp)
        return
    for i in range(n):
        temp.append(s[i])
        solve()
        temp.pop()

solve() 
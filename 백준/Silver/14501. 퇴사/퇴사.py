N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range(N)]

"""점화식
max (solve(i+timeTable[i][0])+timeTable[i][1], solve(i+1))
"""

def solve(i):
    if i>=N:
        return 0
    ret = 0
    if i+timeTable[i][0]<=N :
        ret = solve(i+timeTable[i][0])+timeTable[i][1]
    ret = max(ret,solve(i+1))
    return ret

print(solve(0))
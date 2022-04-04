import sys

sys.setrecursionlimit(1000001)

K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]

lines.sort()
maxLength = 0


def bs(target,start,end):
    global maxLength
    count = 0
    mid = (start+end)//2
    if start>end:
        return None
    for i in lines:
        count+=i//mid
    if count>=target:
        maxLength = max(maxLength,mid)
        return bs(target,mid+1,end)
    elif count<target:
        return bs(target,start,mid-1)

# for i in range(max(lines)): #i는 엄밀히 따지만 잘라진 길이
#     result = bs(N,i,max(lines))
#     if result:
#         print(result)
#         break

result = bs(N,1,max(lines))
print(maxLength)

# 4 4
# 4
# 1
# 5
# 5
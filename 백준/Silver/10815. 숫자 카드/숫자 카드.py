import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
m = int(input())
curious = list(map(int,input().split()))

card.sort()
# curious.sort()

def bs(start,end,target):
    mid = (start+end)//2
    if start>end:
        print(0,end=' ')
        return
    if card[mid] == target:
        print(1,end=' ')
        # print('mid',card[mid], target)
        return mid+1
    elif card[mid] > target:
        bs(start,mid-1,target)
    elif card[mid] < target:
        bs(mid+1,end,target)

# start = bs(0,n-1,curious[0])

for i in range(m):
    # if start >= n-1:
    #     for j in range(i,m):
    #         print(0,end=' ')
    #         break
    bs(0, n-1,curious[i])


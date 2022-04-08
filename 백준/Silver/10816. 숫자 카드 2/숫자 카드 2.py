from collections import defaultdict
N = int(input())

A = list(map(int,input().split()))

A.sort()

A_dict=defaultdict(int)

for i in A:
    A_dict[i]+=1 

M = int(input())
B = list(map(int,input().split()))

result = []

def bs(target,start,end):
    
    if start>end:
        print(0,end=' ')
        return

    mid = (start+end)//2
    if target==A[mid]:
        print(A_dict[target],end=' ')
        return
    elif target>A[mid]:
        return bs(target,mid+1,end)
    else:
        return bs(target,start,mid-1)

for i in B:
    bs(i,0,len(B)-1)
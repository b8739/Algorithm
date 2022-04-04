import sys
sys.setrecursionlimit = 10000000

N = int(input())
n_arr = list(map(int,input().split()))
n_arr.sort()
M = int(input())
m_arr = list(map(int,input().split()))
          
def binary_search(target,start,end):
    if start>end:
        return False
    mid  = (start+end)//2
    if target==n_arr[mid]:
        return True
    elif target>n_arr[mid]:
        return binary_search(target,mid+1,end)
    elif target<n_arr[mid]:
        return binary_search(target,start,mid-1)

for i in m_arr:
    if binary_search(i,0,N-1):
        print(1)
    else:
        print(0)
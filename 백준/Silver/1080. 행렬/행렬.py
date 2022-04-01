"""
알고리즘
루프를 돌면서 A 인덱스 값과 B 인덱스 값을 비교하고 다르면 (A 인덱스 값이 좌측 최상단인) 3x3 부분 행렬을 뒤집는다
다 돌고나서 값이 같다면 count, 아니라면 -1을 출력한다.
"""

def reverse(x,y):
    global A
    for i in range(x,x+3):
        for j in range(y,y+3):
            if A[i][j] == 0:
                 A[i][j] = 1
            else:
                A[i][j] = 0

    
N,M = map(int,input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

count = 0
# A의 값과 B의 값이 동일한지 루프를 돌면서 확인하고, 다르다면 3x3 행렬을 뒤집는다.
for i in range(N-2):
    for j in range(M-2):            
        if A[i][j] != B[i][j]:
            reverse(i,j)
            count+=1
        

# A랑 B가 동일한지 검사
def check():
    for i in range(N):
        for j in range(M): 
            #동일하지 않다면 -1을 출력하고 종료
            if A[i][j] != B[i][j]:
                print(-1)
                return
    #동일하다면 count 값을 출력
    print(count)
check()
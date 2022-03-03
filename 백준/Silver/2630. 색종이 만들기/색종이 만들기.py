#1사분면
#2사분면
#3사분면
#4사분면

#시작점을 잡고 구간안에서 비교한다. 처음 구간은 전체이다.
#만약 시작점과 다른 숫자가 발견된다면, 그건 4분할을 해야 한다는 의미이다.
#4분할을 해준다.
#1사분면 [0:4][0:4]
#2사분면 [0:4][4:8]
#3사분면 [4:8][0:4]
#4사분면 [4:8][4:8]

def solution(x,y,n):
    global white,blue
    start=paper[x][y]
    #처음 시작할 때는 0부터 8까지 (즉 0부터 7까지를 본다)
    for i in range(x,x+n): #세로
    #처음 시작할 때는 0부터 8까지 (즉 0부터 7까지를 본다)
        for j in range(y,y+n): #가로
        #시작점과 다른 점들을 비교
        #만약 시작점과, 그 구간안에서의 다른 점이 다르다면 4분할
            if start!=paper[i][j]:
                solution(x,y,n//2)            #1사분면
                solution(x,y+n//2,n//2)       #2사분면
                solution(x+n//2,y,n//2)       #3사분면
                solution(x+n//2,y+n//2,n//2)  #4사분면
                return
    if start == 0 :
        white+=1
        return
    elif start ==1:
        blue+=1 
        return

N= int(input())
paper=[list(map(int,input().split())) for _ in range (N)]

white,blue = 0,0

solution(0,0,N)
print(white)
print(blue)

"""
시작점과 끝점을 합한 값 (x+n, y+n)을 반복문의 종점으로 잡아줌으로써 8을 벗어나지 않도록 한다.  
x나 y는 0부터 n//2씩 커지더라도, n은 1/2씩 작아지기 때문이다.
대신 시작점이 바뀐다.
"""

# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1
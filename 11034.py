#내가 짠 코드
while True:
    try:
        cnt = 0 
        a,b,c = list(map(int, input().split()))
        
        num = [False] * (c+1) #c개만큼 만들어둠
        
        num[a],num[b],num[c] = True,True,True
        
        pivot = b #2,3,5 
        
        #default
        mover = a
        
        if c-b > b-a:
            method = +1
            mover = a
        else:
            method = -1
            mover = c
        
        while num[pivot+method]==False:
            #중간꺼 앞에 아무것도 없으면 그 앞칸에 min을 넣음
            num[mover],num[pivot+method] = num[pivot+method], num[mover]
            #이제 mid였던 애가 min이 됨
            mover = pivot
            #mid는 기존 숫자 +1 idx가 됐으므로 1을 더해줌
            pivot += method
            #횟수 증가
            cnt += 1
        print (cnt)
    except:
        break
"""
개인소감:
못 풀 줄 알았는데 풀려서 여기서 늘었다고 느꼈다.
배열로 사용하고자 한 아이디어, 그리고 파이썬의 간편한 스왑기능이 머리에 있었기에 쉽게 풀 수 있었다.
근데 다른 사람 코드 보아하니 어처구니 없게 짧다... 후 자괴감이 오지만 배우자
 
주목할 포인트: 
1) a,b,c가 오름차순으로 주어진다.
    1-1) c (최댓값, 어차피 값이 작으므로) 만큼의 배열 (0으로 초기화)을 마련해두고, a,b,c를 idx로 가진 곳은 1을 넣어둔다.
2) 셋 중 하나는 부동이고, 중앙값과 나머지 한 값만 번갈아가면서 이동한다.

풀이 방법:
1) 중앙값인 b는 어떤 경우에든 고정점인 pivot으로 시작한다. (이후에 mover와 역할이 바뀐다)
2) 최대를 구하는 것이기 때문에 두 격차 (b-a vs c-b) 중 큰 쪽으로 한 칸씩 움직이면서 이동횟수를 늘리게 된다 
    3-1) b랑 a간의 격차가 더 크다면, c는 부동, a는 mover, method는 +1이다. (배열의 뒤로 이동) 
    3-2) b랑 c간의 격차가 더 크다면 a는 부동, c는 mover,. method는 -1이다. (배열의 앞으로 이동)
3) while문에서 만약 pivot의 -1 혹은 +1 (3-1 / 3-2에 따라서)이 비어있다면 이동하고 cnt를 늘린다.

"""


#다른 사람 코드
while 1:
    try:
        A, B, C = map(int, input().split())
        print(max(B-A, C-B)-1)
    except:
        break
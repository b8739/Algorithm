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
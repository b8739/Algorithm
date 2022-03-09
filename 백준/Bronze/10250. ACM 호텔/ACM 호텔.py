num = int(input())

for _ in range(num):
    h,w,idx = map(int,input().split()) #6,12,10
    room = idx//h+1 #w: 2
    floor = idx%h #h: 4
    
    if idx % h == 0:  # h의 배수이면,
        floor = h
        room = idx//h
        
    print(f'{floor*100+room}')
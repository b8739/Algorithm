t = int(input())
for n in range(t): #2
    floor = int(input()) # 3
    num = int(input()) # 3
    f0 = [_ for _ in range(1,num+1)] #1,2,3
    
    for f in range(floor):#0부터
        for i in range(1,num): #f[0]은 계속 1이니, f0[1]부터
            f0[i] += f0[i-1] 
    print(f0[-1])
        
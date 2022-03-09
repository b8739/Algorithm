idx = 1
while True:
    res = 0
    
    l,p,v = map(int,input().split())
    
    if l==p==v==0:
        break
    # P일 동안
    res += v//p*l
    
    # P보다 작은 짜투리 기간
    # 1) 해당 기간이 L과 같거나 작을 때
    if l>=v%p:
        res+=v%p
    # 2) 해당 기간이 L보다 클 때
    else:
        res+=l
    print(f'Case {idx}: {res}')
    idx += 1

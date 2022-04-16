N,W = map(int,input().split())
S = [int(input()) for _ in range(N)]
maxv= max(S)
buy_price = maxv
coin = 0

for i in range(N-1):
    #다음꺼가 더 클 때 지금 가격에 구매
    if S[i+1]>S[i]:
        buy_price = min(buy_price,S[i])
        coin = W // buy_price
        minus =  buy_price * coin
    #다음께 작으면 판매
    elif S[i+1]<S[i] and coin != 0:
    #판매
    #돈 차감
        W += S[i]*coin-minus
        buy_price = maxv
        coin=0

if coin!=0:
    W += S[-1]*coin-minus

print(W)



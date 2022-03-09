money = 1000 - int(input())
change = [500,100,50,10,5,1]
cnt = 0

for c in change:
    if money%c == 0:
        cnt+=money//c
        break
    else: 
        cnt += money//c #3
        money = money%c #100
print(cnt)
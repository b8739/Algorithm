n = input() #문자열
total = len(n)
#연속된거 개수 비교 0vs1

cnt = {'0':0,'1':0}
num = n[0]
for i in n[1:]: 
    if num == i :
        continue
    elif num != i:
        cnt[num]+=1
    num = i

cnt[n[-1]] += 1

print(min(list(cnt.values())))



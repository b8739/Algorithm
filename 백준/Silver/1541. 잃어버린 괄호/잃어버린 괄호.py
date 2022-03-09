e = input().split('-')

res = 0

#첫번째 값 넣어둠
for i in e[0].split('+'):
    res+=int(i)
#그 외 값    
for i in e[1:]:
    for j in i.split('+'):
        res -= int(j)
print(res)
n = int(input()) #9
line = 0

while True:
    line+=1
    sum = (line*(line+1))/2
    if sum >= n: #10
        break;
# line: 4
# 그 그룹에서 몇번째인지
idx = n - (line*(line-1)/2)

#짝수
if line % 2 == 0:
    print('%d/%d'%(idx,line-idx+1))
#홀수
else:
    print('%d/%d'%(line-idx+1,idx))
